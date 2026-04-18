import sys
from pathlib import Path
import sys
from pathlib import Path
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
from graph import add_node, add_edge, get_graph
from routing import get_best_path
from health import get_health_status

# Add parent directory to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from shared.schemas import AIResult

app = FastAPI(title="Network Service")

class NodeBatch(BaseModel):
    n: int
    nodes: List[str]

@app.get("/health")
def health():
    return get_health_status()

# 🔥 Add multiple nodes dynamically
@app.post("/add-nodes")
def create_nodes(payload: NodeBatch):
    try:
        if len(payload.nodes) != payload.n:
            raise HTTPException(status_code=400, detail=f"Count mismatch: Expected {payload.n} nodes, but received {len(payload.nodes)}")
        
        for node in payload.nodes:
            add_node(node)
        return {"message": f"{payload.n} nodes added successfully", "nodes": payload.nodes}
    except Exception:
        raise HTTPException(status_code=500, detail="Error adding nodes")

# 🔥 Add edge dynamically
@app.post("/add-edge")
def create_edge(src: str, dst: str, weight: float):
    try:
        add_edge(src, dst, weight)
        return {"message": f"Edge {src}-{dst} added"}
    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))
    except Exception:
        raise HTTPException(status_code=500, detail="Error adding edge")

# 🔥 Get all nodes (for protocol-service later)
@app.get("/nodes")
def get_nodes():
    try:
        G = get_graph()
        return {"nodes": list(G.nodes)}
    except Exception:
        raise HTTPException(status_code=500, detail="Error fetching nodes")

# 🔥 Routing
@app.get("/route")
def route(src: str, dst: str):
    try:
        G = get_graph()
        path = get_best_path(G, src, dst)
        return {"success": True, "path": path}

    except ValueError as ve:
        raise HTTPException(status_code=400, detail=str(ve))

    except Exception:
        raise HTTPException(status_code=500, detail="Internal error")

@app.post("/reroute")
def reroute(result: AIResult):
    """
    Handle reroute decisions from AI service.
    When a node is down or high-risk, reroute traffic around it.
    """
    try:
        node = result.node
        if result.decision == "reroute":
            # Logic to mark node as unavailable for routing
            print(f"[REROUTE] Node {node} marked for reroute. Health: {result.health}, Prediction: {result.prediction}")
            return {"status": "rerouted", "node": node, "decision": result.decision}
        return {"status": "no action needed"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
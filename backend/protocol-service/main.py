import sys
import asyncio
import time
from pathlib import Path
from fastapi import FastAPI
from health import get_health_status
from gossip import run_gossip, node_views
from heartbeat import run_heartbeat

# Add parent directory to path for shared imports
sys.path.insert(0, str(Path(__file__).parent.parent))
from shared.schemas import NodeData

app = FastAPI()

@app.get("/health")
def health():
    return get_health_status()

@app.get("/state")
def get_state():
    return node_views

@app.post("/node-update")
def update_node(data: list[NodeData]):
    try:
        for item in data:
            node = item.node
            if node in node_views:
                for view in node_views.values():
                    if node in view:
                        view[node].update({
                            "health": item.health,
                            "status": item.status,
                            "version": view[node].get("version", 0) + 1,
                            "last_updated": time.time()
                        })
        return {"status": "updated"}
    except Exception as e:
        return {"error": str(e)}

@app.get("/protocol-state")
def get_protocol_state():
    return node_views

@app.on_event("startup")
async def startup():
    asyncio.create_task(run_gossip())
    asyncio.create_task(run_heartbeat())
    asyncio.create_task(run_heartbeat())
import sys
from pathlib import Path
from fastapi import FastAPI
import asyncio
from health import get_health_status
from anomaly import detect_anomaly
from prediction import predict_failure
from scoring import calculate_score
from decision import make_decision
from publisher import publish_result
from analyzer import start_analyzer

sys.path.insert(0, str(Path(__file__).parent.parent))
from shared.schemas import AIResult

app = FastAPI(title="AI Service")

@app.get("/health")
def health():
    return get_health_status()

@app.post("/analyze")
async def analyze(node_data: dict):
    try:
        anomaly = detect_anomaly(node_data)
        prediction = predict_failure(node_data)
        score = calculate_score(node_data)
        decision = make_decision(node_data, prediction, score)
        result = AIResult(
            node=node_data.get("node"),
            health=node_data.get("health"),
            status=node_data.get("status"),
            anomaly=anomaly,
            prediction=prediction,
            score=score,
            decision=decision
        )
        await publish_result(result.dict())
        return {"success": True, "result": result.dict()}
    except Exception as e:
        print("[AI ERROR]", e)
        return {"success": False, "error": "processing failed"}

@app.post("/event")
def handle_event(event: dict):
    print(event)
    return {"success": True}

@app.on_event("startup")
async def startup():
    asyncio.create_task(start_analyzer())

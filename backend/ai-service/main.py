from fastapi import FastAPI
from health import get_health_status
from anomaly import detect_anomaly
from prediction import predict_failure
from scoring import calculate_score
from decision import make_decision
from publisher import publish_result

app = FastAPI(title="AI Service")

@app.get("/health")
def health():
    return get_health_status()

@app.post("/analyze")
def analyze(node_data: dict):
    try:
        anomaly = detect_anomaly(node_data)
        prediction = predict_failure(node_data)
        score = calculate_score(node_data)
        decision = make_decision(node_data, prediction, score)

        result = {
            "node": node_data.get("node"),
            "health": node_data.get("health"),
            "status": node_data.get("status"),
            "anomaly": anomaly,
            "prediction": prediction,
            "score": score,
            "decision": decision
        }

        # send to gateway
        publish_result(result)

        return {
            "success": True,
            "result": result
        }

    except Exception as e:
        print("[AI ERROR]", e)
        return {
            "success": False,
            "error": "processing failed"
        }
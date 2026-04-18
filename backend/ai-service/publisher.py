import requests

API_GATEWAY_URL = "http://127.0.0.1:8000"

def publish_result(data):
    try:
        requests.post(
            f"{API_GATEWAY_URL}/ai-update",
            json=data,
            timeout=2
        )
    except Exception as e:
        print("[PUBLISH ERROR]", e)
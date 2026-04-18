import os

import httpx

API_GATEWAY_URL = os.getenv("API_GATEWAY_URL", "http://api-gateway:8000")


async def publish_result(data):
    try:
        async with httpx.AsyncClient(timeout=2.0) as client:
            await client.post(f"{API_GATEWAY_URL}/ai-update", json=data)
    except Exception as e:
        print("[PUBLISH ERROR]", e)

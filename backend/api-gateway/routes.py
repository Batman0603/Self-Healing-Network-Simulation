from fastapi import APIRouter, HTTPException
from service_calls import fetch_route
from shared.schemas import AIResult
import httpx

router = APIRouter()

@router.get("/get-route")
def get_route(src: str, dst: str):
    try:
        result = fetch_route(src, dst)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ai-update")
def ai_update(result: AIResult):
    # Store or broadcast the AI result
    print("AI Update received:", result.dict())
    return {"status": "received"}

@router.get("/protocol-state")
async def protocol_state():
    try:
        async with httpx.AsyncClient() as client:
            # Fetch from protocol-service asynchronously
            response = await client.get("http://protocol-service:8011/protocol-state", timeout=2.0)
            if response.status_code == 200:
                return response.json()
            return {"error": f"Protocol service returned {response.status_code}"}
    except Exception as e:
        return {"error": str(e)}
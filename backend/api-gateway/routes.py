from fastapi import APIRouter, HTTPException
from service_calls import fetch_route

router = APIRouter()

@router.get("/get-route")
def get_route(src: str, dst: str):
    try:
        result = fetch_route(src, dst)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
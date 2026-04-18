import logging
import os
from fastapi import APIRouter, HTTPException
from typing import Optional
from shared.service_client import ServiceClient

NETWORK_SERVICE_URL = os.getenv("NETWORK_SERVICE_URL", "http://network-service:8001")
PROTOCOL_SERVICE_URL = os.getenv("PROTOCOL_SERVICE_URL", "http://protocol-service:8011")
METRICS_SERVICE_URL = os.getenv("METRICS_SERVICE_URL", "http://metrics-service:8012")
AI_SERVICE_URL = os.getenv("AI_SERVICE_URL", "http://ai-service:8013")
SIMULATION_SERVICE_URL = os.getenv("SIMULATION_SERVICE_URL", "http://simulation-service:8010")
WEBSOCKET_SERVICE_URL = os.getenv("WEBSOCKET_SERVICE_URL", "http://websocket-service:8002")
SERVICE_NAME = os.getenv("SERVICE_NAME", "api-gateway")

logger = logging.getLogger(__name__)
router = APIRouter()


# ===== Network Service Routes =====
@router.post("/network/add-nodes")
async def add_nodes(payload: dict):
    """Add nodes to the network"""
    try:
        result = await ServiceClient.post(f"{NETWORK_SERVICE_URL}/add-nodes", json=payload)
        return result if result else {"error": "Network service unavailable"}
    except Exception as e:
        logger.error(f"[{SERVICE_NAME}] Network add-nodes error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/network/add-edge")
async def add_edge(src: str, dst: str, weight: float):
    """Add edge between nodes"""
    try:
        result = await ServiceClient.post(
            f"{NETWORK_SERVICE_URL}/add-edge",
            json={"src": src, "dst": dst, "weight": weight}
        )
        return result if result else {"error": "Network service unavailable"}
    except Exception as e:
        logger.error(f"[{SERVICE_NAME}] Network add-edge error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/network/nodes")
async def get_nodes():
    """Get all nodes in network"""
    try:
        result = await ServiceClient.get(f"{NETWORK_SERVICE_URL}/nodes")
        return result if result else {"nodes": []}
    except Exception as e:
        logger.error(f"[{SERVICE_NAME}] Network get-nodes error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/network/route")
async def get_route(src: str, dst: str):
    """Get route between two nodes"""
    try:
        result = await ServiceClient.get(f"{NETWORK_SERVICE_URL}/route", params={"src": src, "dst": dst})
        return result if result else {"path": []}
    except Exception as e:
        logger.error(f"[{SERVICE_NAME}] Network get-route error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ===== Protocol Service Routes =====
@router.get("/protocol/state")
async def get_protocol_state():
    """Get protocol state"""
    try:
        result = await ServiceClient.get(f"{PROTOCOL_SERVICE_URL}/state")
        return result if result else {}
    except Exception as e:
        logger.error(f"[{SERVICE_NAME}] Protocol state error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ===== Metrics Service Routes =====
@router.get("/metrics")
async def get_metrics():
    """Get system metrics"""
    try:
        result = await ServiceClient.get(f"{METRICS_SERVICE_URL}/metrics")
        return result if result else {}
    except Exception as e:
        logger.error(f"[{SERVICE_NAME}] Metrics error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ===== AI Service Routes =====
@router.post("/ai/analyze")
async def analyze_node(node_data: dict):
    """Analyze node data using AI"""
    try:
        result = await ServiceClient.post(f"{AI_SERVICE_URL}/analyze", json=node_data)
        return result if result else {"error": "AI service unavailable"}
    except Exception as e:
        logger.error(f"[{SERVICE_NAME}] AI analysis error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ===== Service Health Routes =====
@router.get("/health/all")
async def health_all():
    """Check health of all services"""
    services = {
        "api-gateway": "up",
        "network-service": await ServiceClient.health_check(NETWORK_SERVICE_URL),
        "protocol-service": await ServiceClient.health_check(PROTOCOL_SERVICE_URL),
        "metrics-service": await ServiceClient.health_check(METRICS_SERVICE_URL),
        "ai-service": await ServiceClient.health_check(AI_SERVICE_URL),
        "simulation-service": await ServiceClient.health_check(SIMULATION_SERVICE_URL),
        "websocket-service": await ServiceClient.health_check(WEBSOCKET_SERVICE_URL),
    }

    all_healthy = all(services.values())

    return {
        "status": "healthy" if all_healthy else "degraded",
        "services": services,
        "timestamp": __import__('time').time()
    }


# ===== Broadcast Routes =====
@router.post("/broadcast/alert")
async def broadcast_alert(data: dict):
    """Broadcast alert via WebSocket"""
    try:
        result = await ServiceClient.post(f"{WEBSOCKET_SERVICE_URL}/broadcast/alert", json=data)
        return result if result else {"status": "sent"}
    except Exception as e:
        logger.error(f"[{SERVICE_NAME}] Broadcast alert error: {e}")
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/broadcast/health")
async def broadcast_health(data: dict):
    """Broadcast health update via WebSocket"""
    try:
        result = await ServiceClient.post(f"{WEBSOCKET_SERVICE_URL}/broadcast/health", json=data)
        return result if result else {"status": "sent"}
    except Exception as e:
        logger.error(f"[{SERVICE_NAME}] Broadcast health error: {e}")
        raise HTTPException(status_code=500, detail=str(e))


# ===== Legacy Routes (for backward compatibility) =====
@router.get("/get-route")
def get_route_legacy(src: str, dst: str):
    """Legacy route endpoint"""
    try:
        # This would need the old service_calls implementation
        return {"path": [], "message": "Use /network/route instead"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/ai-update")
def ai_update(result: dict):
    """Legacy AI update endpoint"""
    print("AI Update received:", result)
    return {"status": "received"}

@router.get("/protocol-state")
async def protocol_state_legacy():
    """Legacy protocol state endpoint"""
    return await get_protocol_state()

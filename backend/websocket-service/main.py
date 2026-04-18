from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from manager import ConnectionManager
from health import get_health_status
from socket_handler import send_alert, send_health_update, send_packet_update

app = FastAPI(title="WebSocket Service")

manager = ConnectionManager()

@app.get("/health")
def health():
    return get_health_status()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await manager.send_personal_message(f"Echo: {data}", websocket)
    except WebSocketDisconnect:
        manager.disconnect(websocket)
    except Exception:
        manager.disconnect(websocket)

@app.post("/broadcast/alert")
async def broadcast_alert_endpoint(data: dict):
    await send_alert(data)
    return {"status": "alert sent"}

@app.post("/broadcast/health")
async def broadcast_health_endpoint(data: dict):
    await send_health_update(data)
    return {"status": "health update sent"}

@app.post("/broadcast/packet")
async def broadcast_packet_endpoint(data: dict):
    await send_packet_update(data)
    return {"status": "packet update sent"}
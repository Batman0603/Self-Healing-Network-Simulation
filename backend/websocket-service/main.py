from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from manager import ConnectionManager
from health import get_health_status

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
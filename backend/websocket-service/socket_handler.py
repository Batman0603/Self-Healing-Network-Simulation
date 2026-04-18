from manager import ConnectionManager

manager = ConnectionManager()

async def send_packet_update(data: dict):
    try:
        await manager.broadcast(f"PACKET:{data}")
    except Exception:
        pass

async def send_health_update(data: dict):
    try:
        await manager.broadcast(f"HEALTH:{data}")
    except Exception:
        pass

async def send_alert(data: dict):
    try:
        await manager.broadcast(f"ALERT:{data}")
    except Exception:
        pass
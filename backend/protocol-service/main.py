from fastapi import FastAPI
import asyncio
from health import get_health_status
from gossip import run_gossip
from heartbeat import run_heartbeat

app = FastAPI()

@app.get("/health")
def health():
    return get_health_status()

@app.on_event("startup")
async def startup():
    asyncio.create_task(run_gossip())
    asyncio.create_task(run_heartbeat())
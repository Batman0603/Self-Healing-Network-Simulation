from fastapi import FastAPI
import asyncio
from simulator import run_simulation
from health import get_health

app = FastAPI(title="Simulation Service")

@app.get("/health")
def health():
    return get_health()

@app.on_event("startup")
async def startup():
    asyncio.create_task(run_simulation())
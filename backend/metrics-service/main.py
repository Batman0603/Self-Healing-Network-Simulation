from fastapi import FastAPI
import asyncio
from collector import collect_metrics
from metrics import get_metrics
from health import get_health_status

app = FastAPI(title="Metrics Service")

@app.get("/health")
def health():
    return get_health_status()

@app.get("/metrics")
def metrics():
    return get_metrics()

@app.on_event("startup")
async def startup():
    asyncio.create_task(collect_metrics())
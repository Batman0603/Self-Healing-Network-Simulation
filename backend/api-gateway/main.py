from fastapi import FastAPI
from routes import router

app = FastAPI(title="API Gateway")

app.include_router(router)

@app.get("/health")
def health():
    return {"status": "api-gateway running"}
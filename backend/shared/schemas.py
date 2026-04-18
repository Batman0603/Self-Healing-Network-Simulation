from pydantic import BaseModel, Field

class NodeData(BaseModel):
    node: str = Field(..., example="N1")
    health: float = Field(..., ge=0.0, le=1.0)
    status: str = Field(..., example="alive")


class AIResult(BaseModel):
    node: str
    health: float
    status: str
    anomaly: bool
    prediction: str
    score: int
    decision: str
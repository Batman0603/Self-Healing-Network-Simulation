from pydantic import BaseModel
from typing import Literal
import time

class NetworkEvent(BaseModel):
    node_id: str
    status: Literal["UP", "DOWN"]
    timestamp: float = time.time()
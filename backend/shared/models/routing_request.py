from pydantic import BaseModel
from typing import List

class RoutingRequest(BaseModel):
    source: str
    destination: str
    failed_nodes: List[str]
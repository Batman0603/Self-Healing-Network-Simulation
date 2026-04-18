from pydantic import BaseModel
from typing import List

class AIResponse(BaseModel):
    new_path: List[str]
    confidence: float
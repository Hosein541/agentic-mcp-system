from pydantic import BaseModel
from typing import List, Dict, Any


class Step(BaseModel):
    tool: str
    args: Dict[str, Any]


class Plan(BaseModel):
    steps: List[Step]
from pydantic import BaseModel
from typing import Optional

class ChatRequest(BaseModel):
    question: str
    use_history: Optional[bool] = True
    mode: Optional[str] = "custom"
    conversation_id: Optional[str] = None

class ChatResponse(BaseModel):
    answer: str
    conversation_id: Optional[str] = None
from typing import List
from langchain_core.messages import HumanMessage, AIMessage

system_prompt = """You are a scholarly AI assistant that helps with academic research.
Answer questions in a clear, accurate manner. If you don't know the answer, say you don't know - don't make up answers."""

def update_history(history: List, user_input: str, ai_response: str):
    history.extend([HumanMessage(content=user_input), AIMessage(content=ai_response)])
    return history[-20:]

def get_contextual_history(history: List):
    return [
        {"role": "system", "content": system_prompt},
        *[{"role": "user" if isinstance(msg, HumanMessage) else "assistant", "content": msg.content}
          for msg in history]
    ]
# routers/global_controller.py

from fastapi import APIRouter, HTTPException
from models.chat_models import ChatRequest, ChatResponse
from utils.chat_util import get_contextual_history, update_history
from utils.langchain_util import global_history, llm_global, chat_chain

router = APIRouter(prefix="/api/global", tags=["Global GPT"])

@router.post("/chat", response_model=ChatResponse)
async def global_chat(request: ChatRequest):
    question = request.question.strip()
    if not question:
        raise HTTPException(status_code=400, detail="Please provide a question.")

    try:
        if request.use_history and global_history:
            messages = get_contextual_history(global_history)
            messages.append({"role": "user", "content": question})
            response = await llm_global.ainvoke(messages)
            answer = response.content
        else:
            answer = await chat_chain.ainvoke(question)

        update_history(global_history, question, answer)
        return ChatResponse(answer=answer, conversation_id=request.conversation_id)

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

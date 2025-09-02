from fastapi import APIRouter, HTTPException
from models.chat_models import ChatResponse, ChatRequest

from utils.azure_util import azure_client

router = APIRouter(prefix="/api/azure", tags=["Image GPT"])

@router.post("/image", response_model=ChatResponse)
async def generate_image(request: ChatRequest):
    question = request.question.strip()
    """
    Handle image generation requests and return responses.
    """
    # Placeholder implementation
    if not request.question:
        raise HTTPException(status_code=400, detail="Question is required")
    
    try:
        # Generate the image
        response = azure_client.images.generate(
            model="dall-e-3", # use your deployed model name
            prompt=question,
            n=1,
            size="1024x1024"
        )
        image_url = response.data[0].url
        return ChatResponse(answer=image_url, conversation_id=request.conversation_id)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
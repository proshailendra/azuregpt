from fastapi import APIRouter, HTTPException
from models.chat_models import ChatResponse, ChatRequest

from config.settings import settings
from utils.azure_util import azure_history, azure_client

router = APIRouter(prefix="/api/azure", tags=["Custom GPT"])

@router.post("/chat", response_model=ChatResponse)
async def azure_chat(request: ChatRequest):
    question = request.question.strip()
    """
    Handle chat requests and return responses.
    """
    # Placeholder implementation
    if not request.question:
        raise HTTPException(status_code=400, detail="Question is required")
    
    try:
        azure_history.append({"role":"user", "content":question})  # Reset history for each request
        # Include speech result if speech is enabled
        messages = [{"role": "system", "content": "You are a helpful AI assistant."}, *azure_history]

        # Generate the completion
        response =azure_client.chat.completions.create(
            model=settings.AZURE_OPENAI_DEPLOYMENT,
            messages=messages,
            max_tokens=2048,
            temperature=0.7,
            top_p=0.95,
            frequency_penalty=0,
            presence_penalty=0,
            stop=None,
            stream=False,
            extra_body={
            "data_sources": [{
                "type": "azure_search",
                "parameters": {
                    "endpoint": settings.AZURE_SEARCH_ENDPOINT,
                    "index_name": settings.AZURE_SEARCH_INDEX,
                    "semantic_configuration": f"{settings.AZURE_SEARCH_INDEX}-semantic-configuration",
                    "query_type": "vector_semantic_hybrid",
                    "fields_mapping": {},
                    "in_scope": True,
                    "filter": None,
                    "strictness": 3,
                    "top_n_documents": 5,
                    "authentication": {
                      "type": "api_key",
                      "key": settings.AZURE_SEARCH_KEY
                    },
                    "embedding_dependency": {
                        "type": "deployment_name",
                        "deployment_name": settings.AZURE_EMBEDDING_DEPLOYMENT
                     }
                   }
                }]
            }
        )
        # Simulate a response from Azure OpenAI
        answer = response.choices[0].message.content
        azure_history.append({"role":"assistant", "content":answer})
        return ChatResponse(answer=answer, conversation_id=request.conversation_id)
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Azure RAG Error: {str(e)}")
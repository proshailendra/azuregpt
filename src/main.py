from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import azure_search_controller, global_controller, image_generator_controller

app = FastAPI(
    title="Azure ChatGPT API", 
    version="1.0.0", 
    docs_url="/swagger",
    description="API for Azure ChatGPT with Azure Search integration"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Root endpoint
@app.get("/hello")
async def root():
    return {"message": "Hello from Azure"}

app.include_router(azure_search_controller.router)
app.include_router(global_controller.router)
app.include_router(image_generator_controller.router)
from fastapi import FastAPI

app = FastAPI(
    title="Azure ChatGPT API", 
    version="1.0.0", 
    docs_url="/swagger",
    description="API for Azure ChatGPT with Azure Search integration"
)

# Root endpoint
@app.get("/hello")
async def root():
    return {"message": "Hello from Azure"}

from config.settings import settings
from openai import AzureOpenAI

#History
azure_history = []

# Azure OpenAI Client 
azure_client = AzureOpenAI(
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    api_key=settings.AZURE_OPENAI_KEY,
    api_version=settings.AZURE_OPENAI_VERSION,
)
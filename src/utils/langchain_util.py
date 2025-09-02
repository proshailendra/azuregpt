# LangChain Imports
from langchain_openai import AzureChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

from config.settings import settings

# Prompt
system_prompt = """You are a scholarly AI assistant that helps with academic research.
Answer questions in a clear, accurate manner. If you don't know the answer, say you don't know - don't make up answers."""

# History
global_history = []

# LangChain Global LLM
llm_global = AzureChatOpenAI(
    azure_endpoint=settings.AZURE_OPENAI_ENDPOINT,
    openai_api_version=settings.AZURE_OPENAI_VERSION,
    azure_deployment=settings.AZURE_OPENAI_DEPLOYMENT,
    openai_api_key=settings.AZURE_OPENAI_KEY,
    temperature=0.7,
    max_tokens=2048,
)

# LangChain Prompt Chain
prompt_template = ChatPromptTemplate.from_messages([
    ("system", system_prompt),
    ("human", "{question}")
])

chat_chain = (
    {"question": RunnablePassthrough()}
    | prompt_template
    | llm_global
    | StrOutputParser()
)

from fastapi import FastAPI
from dotenv import load_dotenv
from apps.api.api_v1.router import router

# Load environment variables from .env file
load_dotenv()

app = FastAPI(
    title="ResolveAI Enterprise",
    description="AI-powered issue resolution platform with LangGraph, MCP, and RAG",
    version="1.0.0"
)

app.include_router(router)

from fastapi import APIRouter
from apps.api.api_v1.routes.issues import router as issues_router

router = APIRouter(prefix="/api/v1")

router.include_router(issues_router, prefix="/issues", tags=["Issues"])

from fastapi import APIRouter
from apps.jobs import routers as job_router

api_router = APIRouter()

api_router.include_router(job_router.router, prefix='/jobs', tags=['jobs'])

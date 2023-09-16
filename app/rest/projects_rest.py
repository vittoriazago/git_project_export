from fastapi import APIRouter

from app.integrations.gitlab.gitlab_api import get_projects


BASE_URL = "/projects"

router = APIRouter()


@router.get(
    BASE_URL,
    name="Get projects",
    description="List projects"
)
async def projects(group):
    return await get_projects(group)

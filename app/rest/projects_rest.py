from fastapi import APIRouter

from app.integrations.gitlab.gitlab_api import get_projects


router = APIRouter(prefix="/api/v1/projects", tags=["projects"])


@router.get(
    "",
    name="Get projects",
    description="List projects"
)
async def projects(
    group: str,
    page: int = 1,
    per_page: int = 10,
    archived: bool = False
):
    return await get_projects(group, page, per_page, archived)

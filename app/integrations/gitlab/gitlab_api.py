from typing import Any, Dict, Mapping, Optional

from app.config.app_settings import gitlab_api_settings
from app.integrations.utils.api import send_request


BASE_URL = f'{gitlab_api_settings.base_url}/api/v{gitlab_api_settings.version}'

GET_PROJECTS_URL = "groups/%s/projects"


def _get_headers():
    return {"PRIVATE-TOKEN": gitlab_api_settings.private_token}


async def get_projects(
    group: str,
    page: int = 1,
    per_page: int = 10,
    archived: bool = False
) -> Optional[Mapping[str, Any]]:

    params: Dict[str, Any] = {
        "archived": archived,
        "include_subgroups": True,
        "page": page,
        "per_page": per_page,
        "order_by": "name",
        "sort": "asc",
    }
    url = f'{BASE_URL}/{GET_PROJECTS_URL}' % group

    headers = _get_headers()

    return await send_request(url, "GET", params, headers)

from typing import Any, Mapping, Optional

import httpx
from app.config.app_settings import gitlab_api_settings
from starlette import status

from app.config.exceptions import UnexpectedResponseStatus

BASE_URL = f'{gitlab_api_settings.base_url}/api/v{gitlab_api_settings.version}'

GET_PROJECTS_URL = "groups/{group}/projects"


async def send_request(
    url: str,
    method: str,
    headers: dict,
    payload: Optional[dict] = None,
) -> Optional[Mapping[str, Any]]:

    async with httpx.AsyncClient() as client:
        timeout = httpx.Timeout(10.0, read=None)
        req = client.build_request(method, url, json=payload, headers=headers, timeout=timeout)
        response = await client.send(req, follow_redirects=True)

        if (
            response.status_code == status.HTTP_200_OK
            or response.status_code == status.HTTP_201_CREATED
            or response.status_code == status.HTTP_202_ACCEPTED
        ):
            body = response.json()
            return body

        raise UnexpectedResponseStatus(actual=response.status_code, expected=status.HTTP_200_OK)


def _get_headers():
    return {"PRIVATE-TOKEN": gitlab_api_settings.private_token}


async def get_projects(
    group: str, 
    page: int = 1, 
    per_page: int = 10,
    archived: bool = False
) -> Optional[Mapping[str, Any]]:

    params = f'archived={archived}&include_subgroups=true'    
    pagination = f'&page={page}&per_page={per_page}&order_by=name&sort=asc'
    url = f'{BASE_URL}/{GET_PROJECTS_URL}?{params}{pagination}'.format(group=group)
    
    headers = _get_headers()
    
    return await send_request(url, "GET", headers)

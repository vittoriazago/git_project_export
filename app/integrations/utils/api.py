from typing import Any, Mapping, Optional

import httpx
from starlette import status

from app.config.exceptions import UnexpectedResponseStatus

success_status = [
    status.HTTP_200_OK,
    status.HTTP_201_CREATED,
    status.HTTP_202_ACCEPTED
]


async def send_request(
    url: str,
    method: str,
    params: Optional[dict] = None,
    headers: Optional[dict] = None,
    payload: Optional[dict] = None,
    timeout: int = 10,
) -> Optional[Mapping[str, Any]]:

    async with httpx.AsyncClient() as client:
        timeout = httpx.Timeout(timeout, read=None)
        req = client.build_request(
            method,
            url,
            params=params,
            json=payload,
            headers=headers,
            timeout=timeout
        )
        response = await client.send(req, follow_redirects=True)

        if response.status_code in success_status:
            body = response.json()
            return body

        raise UnexpectedResponseStatus(
            actual=response.status_code,
            expected=status.HTTP_200_OK
        )

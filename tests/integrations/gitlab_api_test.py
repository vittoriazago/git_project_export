from unittest.mock import patch
import pytest
import httpx

from app.integrations.gitlab.gitlab_api import get_projects


@pytest.mark.anyio
@patch(
    'app.integrations.utils.api.httpx.AsyncClient.send',
    return_value=httpx.Response(
        200,
        json=[]
    )
)
async def test_get_projects(mocker):
    result = await get_projects(group="test")
    assert result == []

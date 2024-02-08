from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import Response


def _get_kwargs(
    field_id: int,
) -> Dict[str, Any]:
    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": f"/automations/scheduler/{field_id}/stop",
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.json()
        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, HTTPValidationError]]:
    """Stop Scheduler

     Stop executing a scheduler, then return whether it was stopped.

    Returns:
        A 200 response, if the scheduler was stopped, or a 404 response if no scheduler was found.

    Args:
        field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        field_id=field_id,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, HTTPValidationError]]:
    """Stop Scheduler

     Stop executing a scheduler, then return whether it was stopped.

    Returns:
        A 200 response, if the scheduler was stopped, or a 404 response if no scheduler was found.

    Args:
        field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        field_id=field_id,
        client=client,
    ).parsed


async def asyncio_detailed(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Response[Union[Any, HTTPValidationError]]:
    """Stop Scheduler

     Stop executing a scheduler, then return whether it was stopped.

    Returns:
        A 200 response, if the scheduler was stopped, or a 404 response if no scheduler was found.

    Args:
        field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        field_id=field_id,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    field_id: int,
    *,
    client: Union[AuthenticatedClient, Client],
) -> Optional[Union[Any, HTTPValidationError]]:
    """Stop Scheduler

     Stop executing a scheduler, then return whether it was stopped.

    Returns:
        A 200 response, if the scheduler was stopped, or a 404 response if no scheduler was found.

    Args:
        field_id (int):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            field_id=field_id,
            client=client,
        )
    ).parsed
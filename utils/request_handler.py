from typing import Any, Coroutine

import httpx
import logging
from fastapi import Request, Response

# Logging configuration
logger = logging.getLogger('uvicorn.error')

async def camera_request(request: Request) -> Response:
    try:
        # Retrieve request body
        request_body = await request.body()
        host = request.headers.get("host", "")
        camera_url = f"http://{host}/{request.url.path}"

        # Log request details
        logger.debug(f"Headers of request:\n{request.headers}")
        logger.debug(f"Body of request:\n{request_body.decode('utf-8')}")

        # Forward the request to the camera
        async with httpx.AsyncClient() as client:
            return await client.post(camera_url, headers=request.headers, data=request_body)

    except httpx.RequestError as exc:
        # Handle request errors
        error_message = f"Fail: proxy request: {exc}"
        logger.error(error_message)
        return Response(content=error_message.encode("utf-8"), status_code=500)
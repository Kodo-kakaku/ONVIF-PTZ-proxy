import httpx
import logging
from fastapi import Request, Response

# Logging configuration
logger = logging.getLogger('uvicorn.error')

async def handle_onvif_request(request: Request,
                               modify_response=None) -> Response:
    """
    Function to handle ONVIF requests.
    Receives an incoming HTTP request, forwards it to the camera, and returns the response.
    Allows modifying the response using the provided function.
    """
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
            camera_response = await client.post(camera_url,
                                                headers=request.headers,
                                                data=request_body)

        # Log response details
        logger.debug(f"Headers of response:\n{camera_response.headers}")
        logger.debug(f"Body of response:\n{camera_response.content.decode('utf-8')}")

        # Modify response if needed
        content = camera_response.content
        response_headers = dict(camera_response.headers)
        if modify_response:
            content = modify_response(content)
            response_headers["content-length"] = str(len(content))

        # Return the response to the client
        return Response(
            content=content,
            status_code=camera_response.status_code,
            headers=response_headers,
        )

    except httpx.RequestError as exc:
        # Handle request errors
        error_message = f"Fail: proxy request: {exc}"
        logger.error(error_message)
        return Response(content=error_message.encode("utf-8"), status_code=500)

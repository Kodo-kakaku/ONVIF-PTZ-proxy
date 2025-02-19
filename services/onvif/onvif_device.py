from fastapi import Request, Response
from utils.request_handler import camera_request

async def onvif_device_request(request: Request) -> Response:
    camera_response = await camera_request(request)
    return await Response(
            content=camera_response.content,
            status_code=camera_response.status_code,
            headers=camera_response.headers
        )

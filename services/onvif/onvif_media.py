from fastapi import Request, Response
from utils.request_handler import camera_request

# Function to handle general ONVIF requests
# Receives an incoming HTTP request, forwards it to the camera, and modifies the URI in the response if needed
# ONVIF 2.4

async def onvif_media_request(request: Request) -> Response:
    camera_response = await camera_request(request)
    return await Response(
        content=camera_response.content,
        status_code=camera_response.status_code,
        headers=camera_response.headers
    )

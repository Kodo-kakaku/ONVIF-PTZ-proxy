from utils.xml_utils import modify_uri
from fastapi import Request, Response
from utils.request_handler import camera_request
from utils.xml_utils import modify_uri

# Function to handle general ONVIF requests
# Receives an incoming HTTP request, forwards it to the camera, and modifies the URI in the response if needed
# ONVIF 2.4
async def onvif_request(request: Request) -> Response:
    camera_response = await camera_request(request)

    content = modify_uri(camera_response.content)
    response_headers = dict(camera_response.headers)
    response_headers["content-length"] = str(len(response_headers))

    return await Response(
        content=content,
        status_code=camera_response.status_code,
        headers=camera_response.headers
    )

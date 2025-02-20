from fastapi import Request, Response
from utils.request_handler import camera_request
from utils.xml_utils import extract_pantilt_values
from services.ptz import ptz_service

# Function to handle general ONVIF requests
# Receives an incoming HTTP request, forwards it to the camera, and modifies the URI in the response if needed
# ONVIF 2.4

async def onvif_ptz_request(request: Request) -> Response:
    camera_response = await camera_request(request)

    request_body = await request.body()
    ptz_command = extract_pantilt_values(request_body)
    ptz_service.move(float(ptz_command['x']), float(ptz_command['y']), ptz_command["PanTilt"])

    return Response(
        content=camera_response.content,
        status_code=camera_response.status_code,
        headers=camera_response.headers
    )

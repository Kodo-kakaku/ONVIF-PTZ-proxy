from fastapi import Request, Response

from services.ptz.ptz_service import PtzService
from utils.request_handler import camera_request
from utils.xml_utils import extract_pantilt_values

# Function to handle general ONVIF requests
# Receives an incoming HTTP request, forwards it to the camera, and modifies the URI in the response if needed
# ONVIF 2.4

async def onvif_ptz_request(request: Request) -> Response:
    camera_response = await camera_request(request)

    request_body = await request.body()
    ptz_command = extract_pantilt_values(request_body)

    # Move PTZ pan tilt
    if ptz_command["PanTilt"] is "Start":
        coord_x = float(ptz_command['x'])
        coord_y = float(ptz_command['y'])
        await PtzService.move(coord_x, coord_y)

    return Response(
        content=camera_response.content,
        status_code=camera_response.status_code,
        headers=camera_response.headers
    )

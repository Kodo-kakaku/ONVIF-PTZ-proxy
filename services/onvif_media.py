from fastapi import Request, Response
from utils.request_handler import handle_onvif_request

# Function to handle general ONVIF requests
# Receives an incoming HTTP request, forwards it to the camera, and modifies the URI in the response if needed
# ONVIF 2.4

async def onvif_media_request(request: Request) -> Response:
    return await handle_onvif_request(request)

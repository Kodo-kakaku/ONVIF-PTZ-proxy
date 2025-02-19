from fastapi import APIRouter, Request, Response
# Importing FastAPI components for routing and request handling

from services.onvif import onvif_request
from services.onvif_device_service import onvif_device_request
from services.onvif_media import onvif_media_request
from services.onvif_ptz import onvif_ptz_request
from services.onvif_imaging import onvif_imaging_request
from services.onvif_media_service import onvif_media_service_request
from services.onvif_ptz_service import onvif_ptz_service_request
from services.onvif_imaging_service import onvif_imaging_service_request

# Creating an API router to group ONVIF-related routes
route = APIRouter()

# General proxy route for handling ONVIF requests
@route.post("")
async def onvif_proxy(request: Request) -> Response:
    return await onvif_request(request)

# Route for forwarding requests to ONVIF Device Service
@route.post("/device_service")
async def device_service_proxy(request: Request) -> Response:
    return await onvif_device_request(request)

# Route for forwarding requests to ONVIF Media Service
@route.post("/media_service")
async def media_service_proxy(request: Request) -> Response:
    return await onvif_media_service_request(request)

# Route for forwarding requests to ONVIF PTZ Service
@route.post("/ptz_service")
async def ptz_service_proxy(request: Request) -> Response:
    return await onvif_ptz_service_request(request)

# Route for forwarding requests to ONVIF Imaging Service
@route.post("/imaging_service")
async def imaging_service_proxy(request: Request) -> Response:
    return await onvif_imaging_service_request(request)

# Route for forwarding requests to ONVIF Media API
@route.post('/Media')
async def media_proxy(request: Request):
    return await onvif_media_request(request)

# Route for forwarding requests to ONVIF PTZ API
@route.post('/PTZ')
async def media_proxy(request: Request):
    return await onvif_ptz_request(request)

# Route for forwarding requests to ONVIF Imaging API
@route.post('/Imaging')
async def media_proxy(request: Request):
    return await onvif_imaging_request(request)

from fastapi import APIRouter, Request, Response
from services.onvif.onvif import onvif_request
from services.onvif.onvif_device import onvif_device_request
from services.onvif.onvif_media import onvif_media_request
from services.onvif.onvif_imaging import onvif_imaging_request
from services.onvif.onvif_ptz import onvif_ptz_request


# Creating an API router to group ONVIF-related routes
route = APIRouter()

# Route for forwarding requests to ONVIF
@route.post("/onvif")
@route.post('/onvif/services')
async def onvif_proxy(request: Request) -> Response:
    return await onvif_request(request)

# Route for forwarding requests to ONVIF Device Service
@route.post("/onvif/Device")
@route.post("/onvif/device_service")
async def device_service_proxy(request: Request) -> Response:
    return await onvif_device_request(request)

# Route for forwarding requests to ONVIF Media Service
@route.post('/onvif/Media')
@route.post("/onvif/media_service")
async def media_service_proxy(request: Request) -> Response:
    return await onvif_media_request(request)

# Route for forwarding requests to ONVIF Imaging Service
@route.post('/onvif/Imaging')
@route.post("/onvif/imaging_service")
async def imaging_service_proxy(request: Request) -> Response:
    return await onvif_imaging_request(request)

# Route for forwarding requests to ONVIF PTZ Service
@route.post("/")
@route.post('/onvif/PTZ')
@route.post("/onvif/ptz_service")
async def ptz_service_proxy(request: Request) -> Response:
    return await onvif_ptz_request(request)



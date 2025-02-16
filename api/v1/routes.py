from fastapi import APIRouter, Request, Response
from services.onvif import onvif_request
from services.onvif_device import onvif_device_request
from services.onvif_media import onvif_media_request
from services.onvif_ptz import onvif_ptz_request
from services.onvif_imaging import onvif_imaging_request

route = APIRouter()

@route.post("")
async def onvif_proxy(request: Request) -> Response:
    return await onvif_request(request)

@route.post("/device_service")
async def device_service_proxy(request: Request) -> Response:
    return await onvif_device_request(request)

@route.post('/Media')
async def media_proxy(request: Request):
    return await onvif_media_request(request)

@route.post('/PTZ')
async def media_proxy(request: Request):
    return await onvif_ptz_request(request)

@route.post('/Imaging')
async def media_proxy(request: Request):
    return await onvif_imaging_request(request)
from fastapi import Request, Response
from utils.request_handler import handle_onvif_request

async def onvif_media_request(request: Request) -> Response:
    return await handle_onvif_request(request)

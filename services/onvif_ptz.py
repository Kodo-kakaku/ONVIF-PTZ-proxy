from fastapi import Request, Response
from utils.request_handler import handle_onvif_request
from utils.xml_utils import extract_pantilt_values

async def onvif_ptz_request(request: Request) -> Response:
    request_body = await request.body()
    ptz_command = extract_pantilt_values(request_body)
    print(ptz_command)
    return await handle_onvif_request(request)

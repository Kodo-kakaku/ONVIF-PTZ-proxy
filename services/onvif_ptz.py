from fastapi import Request, Response
from utils.request_handler import handle_onvif_request
from utils.xml_utils import extract_pantilt_values

# Функция обработки общего ONVIF-запроса
# Принимает входящий HTTP-запрос, пересылает его на камеру и может модифицировать URI в ответе
# Версия ONVIF 2.4

async def onvif_ptz_request(request: Request) -> Response:
    request_body = await request.body()
    ptz_command = extract_pantilt_values(request_body)
    #print(ptz_command)
    return await handle_onvif_request(request)

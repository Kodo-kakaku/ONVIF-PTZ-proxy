from fastapi import Request, Response
from utils.request_handler import handle_onvif_request

# Функция обработки общего ONVIF-запроса
# Принимает входящий HTTP-запрос, пересылает его на камеру и может модифицировать URI в ответе
# Версия ONVIF 2.4

async def onvif_imaging_request(request: Request) -> Response:
    return await handle_onvif_request(request)

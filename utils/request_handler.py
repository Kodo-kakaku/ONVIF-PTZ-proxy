import httpx
import logging
from fastapi import Request, Response

# Настройка логирования
logger = logging.getLogger('uvicorn.error')

async def handle_onvif_request(request: Request,
                               modify_response=None) -> Response:
    """
    Функция обработки ONVIF-запросов.
    Принимает входящий HTTP-запрос, пересылает его на камеру и возвращает ответ.
    Позволяет модифицировать ответ с помощью переданной функции.
    """
    try:
        # Получение тела запроса
        request_body = await request.body()
        host = request.headers.get("host", "")
        camera_url = f"http://{host}/{request.url.path}"

        # Логирование запроса
        logger.debug(f"Headers of request:\n{request.headers}")
        logger.debug(f"Body of request:\n{request_body.decode('utf-8')}")

        # Отправка запроса на камеру
        async with httpx.AsyncClient() as client:
            camera_response = await client.post(camera_url,
                                                headers=request.headers,
                                                data=request_body)

        # Логирование ответа
        logger.debug(f"Headers of response:\n{camera_response.headers}")
        logger.debug(f"Body of response:\n{camera_response.content.decode('utf-8')}")

        # Возможное изменение ответа
        content = camera_response.content
        response_headers = dict(camera_response.headers)
        if modify_response:
            content = modify_response(content)
            response_headers["content-length"] = str(len(content))

        # Возвращение ответа клиенту
        return Response(
            content=content,
            status_code=camera_response.status_code,
            headers=response_headers,
        )

    except httpx.RequestError as exc:
        # Обработка ошибки запроса
        error_message = f"Fail: proxy request: {exc}"
        logger.error(error_message)
        return Response(content=error_message.encode("utf-8"), status_code=500)

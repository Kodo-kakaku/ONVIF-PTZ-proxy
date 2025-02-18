import uvicorn
import logging
from fastapi import FastAPI
from api.v1 import routes

# Настройка логирования
logger = logging.getLogger('uvicorn.error')

# Создание экземпляра FastAPI
app = FastAPI(title="ONVIF PTZ Proxy",
              version="1.0.0")

# Подключение маршрутов ONVIF API
app.include_router(routes.route, prefix="/onvif")

# Основная точка входа в приложение
if __name__ == "__main__":
    # Запуск сервера Uvicorn с хостом 0.0.0.0 и портом 80
    uvicorn.run(app, host="0.0.0.0", port=80)

import uvicorn
import logging
from fastapi import FastAPI
from api.v1 import routes

logger = logging.getLogger('uvicorn.error')
app = FastAPI(title="ONVIF PTZ Proxy",
              version="1.0.0")
app.include_router(routes.route, prefix="/onvif")

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=80)

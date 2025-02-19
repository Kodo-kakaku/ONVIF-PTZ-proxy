import uvicorn
import logging
from fastapi import FastAPI
from api.v1 import routes

# Logging configuration
logger = logging.getLogger('uvicorn.error')

# Creating a FastAPI instance
app = FastAPI(title="ONVIF PTZ Proxy",
              version="1.0.0")

# Including ONVIF API routes
app.include_router(routes.route)

# Main application entry point
if __name__ == "__main__":
    # Starting the Uvicorn server with host 0.0.0.0 and port 80
    uvicorn.run(app, host="0.0.0.0", port=80)

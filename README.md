# PTZ Platform ONVIF proxy
This project is necessary to control a turntable made by skilled craftsmen, it deserves your attention!  Currently, the project is in deep development and is not ready for use, stay tuned for news.

## Start project:
1. Install dependencies
    ```
    pip install -r requirements.txt
    ```
2. Start app:
    ```
    uvicorn app.main:app --host 0.0.0.0 --port 80 --log-level info
    ```
## Todo list

- [x] Establish a connection to the camera.
- [x] Receive video stream from camera.
- [ ] Check operation with other cameras.
- [ ] Develop a library to work with PTZ platform.
- [x] Write README.md

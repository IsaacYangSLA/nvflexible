import os
import ssl
import uvicorn

from app.main import app

if __name__ == "__main__":
    tracker_root = os.environ.get("TRACKER_ROOT", "/opt/nvflexible")
    tracker_crt = os.path.join(tracker_root, "cert", "server.crt")
    tracker_key = os.path.join(tracker_root, "cert", "server.key")
    port = os.environ.get("TRACKER_PORT", "8443")
    if os.path.exists(tracker_crt) and os.path.exists(tracker_key):
        ssl_context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
        ssl_context.load_cert_chain(tracker_crt, tracker_key)
        config = uvicorn.Config(app, host="0.0.0.0", port=int(port), ssl_version=ssl.PROTOCOL_TLS_SERVER, ssl_certfile=tracker_crt, ssl_keyfile=tracker_key)
    else:
        config = uvicorn.Config(app, host="0.0.0.0", port=int(port))
        
    server = uvicorn.Server(config)
    server.run()

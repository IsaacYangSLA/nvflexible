bind = "0.0.0.0:8000"
# ca_certs="rootCA.pem"
# cert_reqs=2
# certfile="overseer.crt"
# do_handshake_on_connect=True
# keyfile="overseer.key"
timeout = 30
# worker_class="nvflare.ha.overseer.worker.ClientAuthWorker"
workers = 1
wsgi_app = "nvflexible.tracker.app:app"

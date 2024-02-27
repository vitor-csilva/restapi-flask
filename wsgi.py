from application import create_app
import os
import socket

# Inicialização da API.
if os.getenv("FLASK_ENV") == "development":
    app = create_app("config.DevConfig")
else:
    app = create_app("config.ProdConfig")

ip_address = socket.gethostbyname(socket.gethostname())

# Parte de execução do Script.
if __name__ == "__main__":
    app.run(debug=True, host=ip_address, port=os.getenv("PORT", 5000))

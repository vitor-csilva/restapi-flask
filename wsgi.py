from application import create_app
import os

# Inicialização da API.
if os.getenv('FLASK_ENV') == "development":
    app = create_app('config.DevConfig')
else:
    app = create_app('config.ProdConfig')
# Parte de execução do Script.
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=os.getenv('PORT', 5000))

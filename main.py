from flask import Flask
from routes.auth import routes_auth
from dotenv import load_dotenv
app = Flask(__name__)

# accede a los archivos por medio de los decoradores y anexando el prefijo de la url
app.register_blueprint(routes_auth, url_prefix="/api")

#entri point - funcion principal de ejecucion, ejecuta y levanta servicios del servidor
if __name__ == '__main__':
    load_dotenv()
    app.run(debug=True)
from flask import Blueprint, request, jsonify
from jwt_test import write_token, validate_token

# accede a las funciones para generar las rutas de la api por medio del decorador generado routes_auth
routes_auth = Blueprint("routes_auth", __name__)

#ruta que permite pasarle por metodo post un json con el username y la password
@routes_auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    # en caso de ser correcta la el user se genera el token de lo contrario se enviara un error
    if data['username'] == "Cristian_Santiago":
        return write_token(data=request.get_json())
    else:
        response = jsonify({"message": "User not found"})
        response.status_code = 404
        return response

# se obtiene el token y se valida
@routes_auth.route("/verify/token")
def verify():
    token = request.headers['Authorization'].split(" ")[1]
    return validate_token(token, output=True)
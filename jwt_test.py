from jwt import encode, decode
from jwt import exceptions
from os import getenv
from datetime import datetime, timedelta
from flask import jsonify

# se le asigna la cantidad de dias que tiene el token de vigencia, y retorna el tiempo 
def expire_date(days: int):
    now = datetime.now()
    new_date = now + timedelta(days)
    return new_date

# genera el token codificando la data y pasando parametros como su llave secreta al payload, el uso del algoritmo de encriptacion el tiempo de expiracion del token.
def write_token(data: dict):
    token = encode(payload={**data, "exp": expire_date(1)},key=getenv("SECRET"), algorithm="HS256")
    return token.encode("UTF-8")

# valida el token y decodifica la su encriptacion devolviendo la data almacenada
def validate_token(token, output=False):
    try:
        if output:
            return decode(token, key=getenv("SECRET"), algorithms="HS256")
        decode(token, key=getenv("SECRET"), algorithms="HS256")
    #en caso de generarse excepciones por un token invalido o que haya superado su valides por tiempo genera una respuesta segun el error como respuesta
    except exceptions.DecodeError:
        response = jsonify({"message": "Invalid Token"})
        response.status_code = 401
        return response
    except exceptions.ExpiredSignatureError:
        response = jsonify({"message": "Token Expired"})
        response.status_code = 401
        return response
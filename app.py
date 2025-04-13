from flask import Flask, request
from flasgger import Swagger
from utils.cargar_datos import cargar_ferraris
from filters.filtros import *

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API de Ferrari",
        "description": "API educativa para la materia Taller de Programación",
        "version": "1.0.0",
        "autor": "Matias Sio Cordich",
    }
}

app = Flask(__name__)
swagger = Swagger(app, template=swagger_template)

@app.route('/')
def main():

    """
    Página principal de la API Ferrari
    ---
    tags:
     - Página principal
    responses:
      200:
        description: Información básica de la API
        examples:
          application/json:
            {
              "Message": "Bienvenidxs a la API de Ferrari",
              "Autor": "Matias Sio Cordich",
              "Description": "Esta es una API construida por motivos educativos para la materia de Taller de Programación"
            }
    """
    
    return {
        "Message" : "Bienvenidxs a la API de Ferrari",
        "Autor": "Matias Sio Cordich",
        "Description": "Esta es una API construida por motivos educativos para la materia de Taller de Programación"
        }

# [GET] - Obtener todas las Ferraris
@app.route('/ferrari/all')
def get_Ferraris():

    """
    Obtener todas las Ferraris
    ---
     tags:
      - Listar Ferraris
     responses:
      200:
        description: Lista de todas las Ferraris. A continuación se muestra una estructura de los objetos que se muestran en la respuesta. 
        schema:
          type: array
          items:
            type: object
            properties:
              id:
                type: integer
                example: 1
              modelo:
                type: string
                example: Ferrari 125 S
              anio:
                type: integer
                example: 1947
              tipo_de_automovil:
                type: string
                example: Deportivo
              caballos_de_fuerza:
                type: integer
                example: 118
              tipo_de_motor:
                type: string
                example: V12
              velocidad_maxima:
                type: integer
                example: 180
              aceleracion:
                type: number
                format: float
                example: 8.0
    """
    
    # Traemos todas las Ferraris
    data = cargar_ferraris()
    return data

# [GET] - Obtener una Ferrari por su id
@app.route('/ferrari/id/<int:id_ferrari>')
def get_Ferrari_by_id(id_ferrari):
    
    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()
       
    # Llamamos a la función filtrar_por_id, le pasamos el JSON y el id
    res = filtrar_por_id(data, id_ferrari)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferrari no encontrada'}, 404
    
# [GET] - Obtener una Ferrari por su modelo
@app.route('/ferrari/model/<string:model>')
def get_Ferrari_by_model(model):
    
    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_modelo, le pasamos el JSON y el modelo
    res = filtrar_por_modelo(data, model)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferrari no encontrada'}, 404

# [GET] - Obtener una Ferrari por su año
@app.route('/ferrari/year/<int:year>')
def get_Ferrari_by_year(year):

    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_anio, le pasamos el JSON y el año
    res = filtrar_por_anio(data, year)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferrari no encontrada'}, 404

# [GET] - Obtener Ferraris por tipo de auto
@app.route('/ferrari/type/<string:type>')
def get_Ferraris_by_type(type):

    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_tipo, le pasamos el JSON y el tipo de auto
    res = filtrar_por_tipo(data, type)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferraris no encontradas'}, 404

# [GET] - Obtener Ferraris por cantidad de caballos de fuerza
@app.route('/ferrari/hp/<int:hp>')
def get_Ferraris_by_hp(hp):
    
    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_caballos, le pasamos el JSON y los caballos de fuerza
    res = filtrar_por_caballos(data, hp)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferraris no encontradas'}, 404

# [GET] - Obtener Ferraris por velocidad maxima
@app.route('/ferrari/velocity/<int:velocity>')
def get_Ferraris_by_velocity(velocity):
    
    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_velocidad, le pasamos el JSON y la velocidad
    res = filtrar_por_velocidad(data, velocity)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferraris no encontradas'}, 404

# [GET] - Obtener Ferraris por aceleración
@app.route('/ferrari/acceleration/<float:acceleration>')
def get_Ferraris_by_acceleration(acceleration):
    
    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_aceleracion, le pasamos el JSON y la aceleracion
    res = filtrar_por_aceleracion(data, acceleration)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferraris no encontradas'}, 404

# [GET] - Obtener Ferraris por un rango de años
@app.route('/ferrari/year/range')
def get_Ferraris_by_year_range():

    # Creamos las query params
    min_year = request.args.get('min', type=int)
    max_year = request.args.get('max', type=int)

    # Validamos que el valor máximo no sea menor que el valor minimo
    if max_year <= min_year:
      return {'message' : 'El valor maximo no puede ser menor que el minimo'}, 400
    
    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_rango_anios, le pasamos el JSON y los valores máximos y mínimos
    res = filtra_por_rango_anios(data, min_year, max_year)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferraris no encontradas'}, 404

# [GET] - Obtener Ferraris por un rango de velocidad
@app.route('/ferrari/velocity/range')
def get_Ferraris_by_velocity_range():

    # Creamos las query params
    min_velocidad = request.args.get('min', type=int)
    max_velocidad = request.args.get('max', type=int)

    # Validamos que el valor máximo no sea menor que el valor minimo
    if max_velocidad <= min_velocidad:
      return {'message' : 'El valor maximo no puede ser menor que el minimo'}, 400
    
    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_rango_velocidad, le pasamos el JSON y los valores máximos y mínimos
    res = filtra_por_rango_velocidad(data, min_velocidad, max_velocidad)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferraris no encontradas'}, 404

# [GET] - Obtener Ferraris por un rango de caballos de fuerza
@app.route('/ferrari/hp/range')
def get_Ferraris_by_hp_range():

    # Creamos las query params
    min_hp = request.args.get('min', type=int)
    max_hp = request.args.get('max', type=int)

    # Validamos que el valor máximo no sea menor que el valor minimo
    if max_hp <= min_hp:
      return {'message' : 'El valor maximo no puede ser menor que el minimo'}, 400
    
    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_rango_caballos, le pasamos el JSON y los valores máximos y mínimos
    res = filtra_por_rango_caballos(data, min_hp, max_hp)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferraris no encontradas'}, 404

# [GET] - Obtener Ferraris por un rango de aceleracion 
@app.route('/ferrari/acceleration/range')
def get_Ferraris_by_acc_range():

    # Creamos las query params
    min_acc = request.args.get('min', type=float)
    max_acc = request.args.get('max', type=float)

    # Validamos que el valor máximo no sea menor que el valor minimo
    if max_acc <= min_acc:
      return {'message' : 'El valor maximo no puede ser menor que el minimo'}, 400
    
    # Cargamos todo el JSON que contiene la información
    data = cargar_ferraris()

    # Llamamos a la función filtrar_por_rango_aceleracion, le pasamos el JSON y los valores máximos y mínimos
    res = filtra_por_rango_aceleracion(data, min_acc, max_acc)

    # Validamos el resultado de la búsqueda
    if res:
        return res,202

    # Si no se encontró ningun valor que me devuelva un mensaje
    return {'message' : 'Ferraris no encontradas'}, 404


if __name__ == '__main__':
    app.run(debug=True)
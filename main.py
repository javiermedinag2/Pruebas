#libreria flask para crear la api REST
from flask import Flask, request, jsonify

#funcion que recibe la temperatura y devuelve el clima correspondiente
def clima(temperatura):
    if temperatura < 0:
        return "Helando"
    elif 0 <= temperatura < 10:
        return "Frio"
    elif 10 <= temperatura < 20:
        return "Fresco"
    elif 20 <= temperatura < 30:
        return "Caluroso"
    else:
        return "Caliente"

# Creación de la aplicación Flask
app = Flask(__name__)

# Rutas de la API
@app.route('/')
def index():
    bienvenida = "<H1> Bienvenido a la API de Clima </H1>"
 
    return bienvenida,200

@app.route('/clima', methods=['POST'])
def obtener_clima():
    data = request.get_json()
    temperatura = data.get('temperatura')
    if temperatura is None:
        return jsonify({'error': 'La temperatura es requerida'}), 400
    clima_result = clima(temperatura)
    return jsonify({'clima': clima_result}),200

@app.route('/clima', methods=['GET'])
def obtener_clima_get():
    temperatura = request.args.get('temperatura')
    if temperatura is None:
        return jsonify({'error': 'La temperatura es requerida'}), 400
    clima_result = clima(float(temperatura))
    return jsonify({'clima': clima_result}),200


# Iniciar la aplicación Flask
if __name__ == '__main__':
    app.run(debug=True, port=80)

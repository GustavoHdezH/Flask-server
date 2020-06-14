from flask import Flask, request, jsonify
from app import app
# De la carpeta app importa todo
@app.route('/test', methods=['GET']) # Metodd HTTP para petición
def test():
    return jsonify({"respuesta":"Prueba Exitosa"})
    # Se regresa una respuesta en formato de json y se requiere
    # de la libreria jsonify

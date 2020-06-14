from flask import Flask, request, jsonify
from app import app

@app.route('/test', methods=['GET']) 
def test():
    return jsonify({"respuesta":"Prueba Exitosa"})
from flask import Flask, request
# Se importa el framework y la libreria
app = Flask(__name__)
from app import routes
# De ca carpeta app importa el archivo routes.py

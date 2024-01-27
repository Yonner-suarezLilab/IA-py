# app/app.py
from flask import Flask, render_template
from .extensions import api, socketio
from flask_cors import CORS
from .routes.router_empleado import Empleados
from.routes.router_empleador import Empleadores
from .routes.router_chat import Chat
from .Utils.db import db
from .config import SQLALCHEMY_DATABASE_URI

app = Flask(__name__)
api.init_app(app)

# Definiendo mi ruta de Inicio
@app.route('/')
def index():
    lista_mensajes =  []
    return render_template('public/inicio.html', lista_mensajes=lista_mensajes)

app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

with app.app_context():
    db.create_all()

CORS(app, resources={r"/*": {"origins": "*"}})

api.add_namespace(Empleados, path='')
api.add_namespace(Empleadores, path='')
api.add_namespace(Chat, path='')

from .extensions import socketio  # Importa socketio después de crear la instancia de la aplicación

socketio.init_app(app)

@socketio.on('connect')
def handle_connect():
    print('Cliente conectado')

@socketio.on('disconnect')
def handle_disconnect():
    print('Cliente desconectado')

@socketio.on('mensaje_chat')
def recibir_mensaje(mensaje_chat):
    socketio.emit('mensaje_chat', broadcast=True)


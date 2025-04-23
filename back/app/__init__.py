from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables del archivo .env

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend

# Configuración de conexiones (se usará en routes.py)
app.config['MYSQL_CONFIG'] = {
    'host': os.getenv('MYSQL_HOST'),
    'user': os.getenv('MYSQL_USER'),
    'password': os.getenv('MYSQL_PASSWORD'),
    'database': os.getenv('MYSQL_DATABASE')
}

app.config['POSTGRES_CONFIG'] = {
    'host': os.getenv('POSTGRES_HOST'),
    'user': os.getenv('POSTGRES_USER'),
    'password': os.getenv('POSTGRES_PASSWORD'),
    'database': os.getenv('POSTGRES_DATABASE')
}

app.config['SQLSERVER_CONFIG'] = {
    'driver': os.getenv('SQLSERVER_DRIVER'),
    'server': os.getenv('SQLSERVER_HOST'),
    'database': os.getenv('SQLSERVER_DATABASE'),
    'uid': os.getenv('SQLSERVER_USER'),
    'pwd': os.getenv('SQLSERVER_PASSWORD')
}

from app import routes  # Importar rutas al final para evitar circular imports
from flask import Flask
from flask_cors import CORS
import os
from dotenv import load_dotenv

load_dotenv()  # Carga variables del archivo .env

app = Flask(__name__)
CORS(app)  # Permite peticiones desde el frontend

# Ejemplo de configuración (usando nombres de servicio)
app.config['MYSQL_CONFIG'] = {
    'host': 'mysql_db',  # Nombre del servicio en docker-compose.yml
    'user': 'root',
    'password': 'mysql_password',
    'database': 'ventas_mysql'
}

app.config['POSTGRES_CONFIG'] = {
    'host': 'postgres_db',  # Nombre del servicio
    'user': 'postgres',
    'password': 'postgres_password',
    'database': 'postgres'
}

app.config['SQLSERVER_CONFIG'] = {
    'driver': 'ODBC Driver 17 for SQL Server',
    'server': 'sqlserver_db',  # Nombre del servicio
    'database': 'master',
    'uid': 'sa',
    'pwd': 'SqlServerPassword123!'
}

from app import routes  # Importar rutas al final para evitar circular imports
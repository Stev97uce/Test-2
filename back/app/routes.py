from app import app
from flask import jsonify
import mysql.connector
import psycopg2
import pyodbc

# Conexión a MySQL
def get_mysql_connection():
    return mysql.connector.connect(**app.config['MYSQL_CONFIG'])

# Conexión a PostgreSQL
def get_postgres_connection():
    return psycopg2.connect(**app.config['POSTGRES_CONFIG'])

# Conexión a SQL Server
def get_sqlserver_connection():
    connection_string = f"DRIVER={app.config['SQLSERVER_CONFIG']['driver']};SERVER={app.config['SQLSERVER_CONFIG']['server']};DATABASE={app.config['SQLSERVER_CONFIG']['database']};UID={app.config['SQLSERVER_CONFIG']['uid']};PWD={app.config['SQLSERVER_CONFIG']['pwd']}"
    return pyodbc.connect(connection_string)

# Rutas
@app.route('/clientes', methods=['GET'])
def get_clientes():
    try:
        conn = get_mysql_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM clientes")
        result = cursor.fetchall()
        cursor.close()
        conn.close()
        return jsonify({'clientes': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/productos', methods=['GET'])
def get_productos():
    try:
        conn = get_postgres_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM productos")
        result = cursor.fetchall()
        # Convertir a lista de diccionarios
        productos = [{'id': row[0], 'nombre': row[1], 'precio': float(row[2])} for row in result]
        cursor.close()
        conn.close()
        return jsonify({'productos': productos})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/pedidos', methods=['GET'])
def get_pedidos():
    try:
        conn = get_sqlserver_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM pedidos")
        columns = [column[0] for column in cursor.description]
        result = [dict(zip(columns, row)) for row in cursor.fetchall()]
        cursor.close()
        conn.close()
        return jsonify({'pedidos': result})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
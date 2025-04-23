-- Crear tabla de productos
CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(50) NOT NULL,
    precio DECIMAL(10, 2) CHECK (precio > 0)
);

-- Insertar un registro de ejemplo
INSERT INTO productos (nombre, precio) VALUES ('Laptop', 1500.99);
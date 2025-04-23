-- Crear tabla de pedidos (relaciona clientes y productos)
CREATE TABLE pedidos (
    id INT PRIMARY KEY IDENTITY(1,1),
    cliente_id INT NOT NULL,
    producto_id INT NOT NULL,
    fecha DATE DEFAULT GETDATE()
);

-- Insertar un registro de ejemplo
INSERT INTO pedidos (cliente_id, producto_id, fecha) VALUES (1, 1, '2023-10-01');
document.addEventListener('DOMContentLoaded', function() {
    // Endpoints del backend
    const API_URLS = {
        clientes: 'http://backend:5000/clientes',
        productos: 'http://backend:5000/productos',
        pedidos: 'http://backend:5000/pedidos'
    };

    // Función para cargar datos de clientes
    async function cargarClientes() {
        try {
            const response = await fetch(API_URLS.clientes);
            const data = await response.json();
            
            const tbody = document.querySelector('#tabla-clientes tbody');
            tbody.innerHTML = '';
            
            data.clientes.forEach(cliente => {
                const tr = document.createElement('tr');
                tr.innerHTML = `
                    <td>${cliente.id}</td>
                    <td>${cliente.nombre}</td>
                    <td>${cliente.email}</td>
                `;
                tbody.appendChild(tr);
            });
        } catch (error) {
            console.error('Error cargando clientes:', error);
        }
    }

    // Cargar todos los datos al iniciar
    cargarClientes();
});
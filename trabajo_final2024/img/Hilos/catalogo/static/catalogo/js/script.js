// Asegúrate de que el DOM esté completamente cargado
document.addEventListener("DOMContentLoaded", function() {
    // Manejar clics en los botones de agregar al carrito
    document.querySelectorAll('.agregar-carrito-btn').forEach(btn => {
        btn.addEventListener('click', function() {
            const productId = this.getAttribute('data-product-id');
            fetch(`/agregar-al-carrito/${productId}/`, {
                method: 'GET',
                headers: {
                    'X-Requested-With': 'XMLHttpRequest'
                }
            }).then(response => {
                if (response.ok) {
                    // Opcional: Actualizar el carrito o mostrar un mensaje
                }
            });
        });
    });

    // Manejar el cambio de color de los precios cuando se agregan al carrito
    function agregarAlCarrito(idPrecio) {
        var elementoPrecio = document.getElementById(idPrecio);
        // Cambia el color del precio a verde para indicar que se agregó al carrito
        if (elementoPrecio) {
            elementoPrecio.classList.add('agregado');
        }
    }

    // Si tienes un elemento para mostrar el total del carrito
    let totalCarrito = 0;
    function actualizarTotal(precio) {
        totalCarrito += precio;
        document.getElementById('total-carrito').textContent = `$${totalCarrito.toFixed(2)}`;
    }
});

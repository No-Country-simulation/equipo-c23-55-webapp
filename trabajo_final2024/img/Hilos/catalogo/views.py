from django.shortcuts import render, redirect, get_object_or_404
from .models import Producto
from django.core.mail import send_mail
from django.http import HttpResponse

def inicio(request):
    return render(request, 'catalogo/inicio.html')

def productos(request):
    return render(request, 'catalogo/productos.html')

def contacto(request):
    return render(request, 'catalogo/contacto.html')

def carrito(request):
    carrito = request.session.get('carrito', {})
    total = sum(item['precio'] * item['cantidad'] for item in carrito.values())
    return render(request, 'catalogo/carrito.html', {'carrito': carrito, 'total': total})

def test_view(request):
    return render(request, 'catalogo/test.html')

def como_comprar(request):
    return render(request, 'catalogo/como_comprar.html')

def buscar(request):
    query = request.GET.get('q')
    if query:
        resultados = Producto.objects.filter(nombre__icontains=query)
    else:
        resultados = []
    return render(request, 'catalogo/buscar.html', {'resultados': resultados, 'query': query})

def agregar_al_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    if producto_id in carrito:
        carrito[producto_id]['cantidad'] += 1
    else:
        producto = get_object_or_404(Producto, id=producto_id)
        carrito[producto_id] = {
            'nombre': producto.nombre,
            'precio': producto.precio,
            'cantidad': 1
        }
    request.session['carrito'] = carrito
    return redirect('productos')

def procesar_contacto(request):
    if request.method == 'POST':
        nombre = request.POST.get('nombre')
        email = request.POST.get('email')
        telefono = request.POST.get('telefono', '')
        direccion = request.POST.get('direccion')
        ciudad = request.POST.get('ciudad')
        codigo_postal = request.POST.get('codigo_postal')
        comentarios = request.POST.get('comentarios', '')
        metodo_pago = request.POST.get('metodo_pago')

        mensaje = f"""
        Nombre: {nombre}
        Correo: {email}
        Teléfono: {telefono}
        Dirección: {direccion}, {ciudad}, {codigo_postal}
        Método de Pago: {metodo_pago}
        Comentarios: {comentarios}
        """

        send_mail(
            'Nuevo contacto desde la tienda',
            mensaje,
            'tienda@example.com',
            [email],
            fail_silently=False,
        )

        return HttpResponse("Formulario procesado exitosamente.")
    
    return render(request, 'catalogo/contacto.html')

def procesar_envio(request):
    if request.method == 'POST':
        envio = request.POST['envio']
        request.session['envio'] = envio
        return redirect('procesar_pago')
    
def procesar_pago(request):
    if request.method == 'POST':
        pago = request.POST['pago']
        request.session['pago'] = pago
        return redirect('finalizar_compra')

def finalizar_compra(request):
    send_mail(
        'Confirmación de Compra',
        'Gracias por tu compra.',
        'tienda@example.com',
        [request.session.get('contacto', {}).get('email', '')],
        fail_silently=False,
    )
    return render(request, 'catalogo/compra_exitosa.html')
def checkout(request):
    # Lógica para la vista de checkout
    return render(request, 'catalogo/checkout.html')

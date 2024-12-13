from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('productos/', views.productos, name='productos'),
    path('contacto/', views.contacto, name='contacto'),
    path('carrito/', views.carrito, name='carrito'),
    path('test/', views.test_view, name='test'),
    path('como_comprar/', views.como_comprar, name='como_comprar'),
    path('buscar/', views.buscar, name='buscar'),
    path('agregar_al_carrito/<int:producto_id>/', views.agregar_al_carrito, name='agregar_al_carrito'),
    path('procesar_contacto/', views.procesar_contacto, name='procesar_contacto'),
    path('procesar_envio/', views.procesar_envio, name='procesar_envio'),
    path('procesar_pago/', views.procesar_pago, name='procesar_pago'),
    path('finalizar_compra/', views.finalizar_compra, name='finalizar_compra'),
    path('checkout/', views.checkout, name='checkout'),
]

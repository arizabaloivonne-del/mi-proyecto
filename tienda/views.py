from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.core.mail import send_mail
from django.template.loader import render_to_string
from .models import Producto, CarritoItem, Pedido, PedidoItem

# Vistas de productos
def collares(request):
    productos = Producto.objects.filter(categoria='collares')
    return render(request, 'collares.html', {'productos': productos})

def anillos(request):
    productos = Producto.objects.filter(categoria='anillos')
    return render(request, 'anillos.html', {'productos': productos})

def aretes(request):
    productos = Producto.objects.filter(categoria='aretes')
    return render(request, 'aretes.html', {'productos': productos})

def pulseras(request):
    productos = Producto.objects.filter(categoria='pulseras')
    return render(request, 'pulseras.html', {'productos': productos})

# Vista para agregar productos al carrito
@login_required
def agregar_al_carrito(request, producto_id):
    producto = get_object_or_404(Producto, id=producto_id)
    item, creado = CarritoItem.objects.get_or_create(usuario=request.user, producto=producto)
    if not creado:
        item.cantidad += 1
        item.save()
    return redirect('ver_carrito')

# Vista del carrito
@login_required
def ver_carrito(request):
    items_raw = CarritoItem.objects.filter(usuario=request.user)
    items = []
    total = 0
    for item in items_raw:
        subtotal = item.producto.precio * item.cantidad
        total += subtotal
        items.append({
            'producto': item.producto,
            'cantidad': item.cantidad,
            'subtotal': subtotal
        })
    return render(request, 'carrito.html', {'items': items, 'total': total})

# Actualizar cantidad
@require_POST
@login_required
def actualizar_cantidad(request, producto_id):
    nueva_cantidad = int(request.POST.get('cantidad', 1))
    item = get_object_or_404(CarritoItem, usuario=request.user, producto_id=producto_id)
    if nueva_cantidad > 0:
        item.cantidad = nueva_cantidad
        item.save()
    else:
        item.delete()
    return redirect('ver_carrito')

# Quitar producto
@require_POST
@login_required
def quitar_del_carrito(request, producto_id):
    CarritoItem.objects.filter(usuario=request.user, producto_id=producto_id).delete()
    return redirect('ver_carrito')

# Checkout
@login_required
def checkout(request):
    items_raw = CarritoItem.objects.filter(usuario=request.user)
    items = []
    total = 0
    for item in items_raw:
        subtotal = item.producto.precio * item.cantidad
        total += subtotal
        items.append({
            'producto': item.producto,
            'cantidad': item.cantidad,
            'subtotal': subtotal
        })
    return render(request, 'checkout.html', {'items': items, 'total': total})

# Confirmar pedido con envío de correo HTML
@require_POST
@login_required
def confirmar_pedido(request):
    carrito = CarritoItem.objects.filter(usuario=request.user)

    if not carrito.exists():
        return redirect('ver_carrito')

    total = sum(item.producto.precio * item.cantidad for item in carrito)

    pedido = Pedido.objects.create(usuario=request.user, total=total)

    for item in carrito:
        PedidoItem.objects.create(
            pedido=pedido,
            producto=item.producto,
            cantidad=item.cantidad,
            precio_unitario=item.producto.precio
        )

    carrito.delete()

    # ✅ Enviar correo de confirmación en HTML
    asunto = f"Confirmación de pedido #{pedido.id}"
    mensaje_html = render_to_string('correo_confirmacion.html', {'pedido': pedido})
    destinatario = [request.user.email]

    send_mail(
        subject=asunto,
        message="Tu pedido ha sido confirmado. Revisa los detalles en el correo HTML.",
        from_email=None,  # usa DEFAULT_FROM_EMAIL de settings.py
        recipient_list=destinatario,
        fail_silently=False,
        html_message=mensaje_html  # ✅ esto activa el diseño HTML
    )

    # Redirige al ticket
    return redirect('confirmacion_pedido', pedido_id=pedido.id)

# Ticket de confirmación
@login_required
def confirmacion_pedido(request, pedido_id):
    pedido = get_object_or_404(Pedido, id=pedido_id)
    return render(request, 'confirmacion.html', {'pedido': pedido})

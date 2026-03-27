from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Producto, Pedido, DetallePedido
from .forms import RegistroForm


# LOGIN

def login_view(request):

    if request.method == 'POST':

        user = request.POST['username']
        password = request.POST['password']

        usuario = authenticate(
            request,
            username=user,
            password=password
        )

        if usuario:
            login(request, usuario)
            return redirect('dashboard')

    return render(request, 'login.html')


# REGISTRO

def registro(request):

    form = RegistroForm(request.POST or None)

    if form.is_valid():

        user = form.save(commit=False)
        user.set_password(
            form.cleaned_data['password']
        )
        user.save()

        return redirect('login')

    return render(
        request,
        'registro.html',
        {'form': form}
    )


# LOGOUT

@login_required
def salir(request):

    logout(request)

    return redirect('login')


# DASHBOARD

@login_required
def dashboard(request):

    return render(
        request,
        'dashboard.html'
    )


# PRODUCTOS

@login_required
def productos(request):

    productos = Producto.objects.all()

    return render(
        request,
        'productos.html',
        {
            'productos': productos
        }
    )


# NUEVO PEDIDO

@login_required
def nuevo_pedido(request):

    productos = Producto.objects.all()

    if request.method == 'POST':

        pedido = Pedido.objects.create(
            usuario=request.user
        )

        for p in productos:

            cantidad = request.POST.get(
                str(p.id)
            )

            if cantidad:

                cantidad = int(cantidad)

                if cantidad > 0:

                    DetallePedido.objects.create(
                        pedido=pedido,
                        producto=p,
                        cantidad=cantidad
                    )

                    p.stock -= cantidad
                    p.save()

        return redirect('pedidos')

    return render(
        request,
        'pedido.html',
        {
            'productos': productos
        }
    )


# HISTORIAL PEDIDOS

@login_required
def pedidos(request):

    pedidos = Pedido.objects.filter(
        usuario=request.user
    )

    return render(
        request,
        'pedidos.html',
        {
            'pedidos': pedidos
        }
    )
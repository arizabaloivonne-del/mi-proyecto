from django.shortcuts import render, redirect
from django.contrib.auth import login
from .forms import CustomUserCreationForm, EmailLoginForm

# Vista principal
def inicio(request):
    return render(request, 'index.html')

# Registro
def crear_cuenta(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'registration/crear_cuenta.html', {'form': form})

# Login con email
def login_con_email(request):
    if request.method == 'POST':
        form = EmailLoginForm(request.POST)
        if form.is_valid():
            user = form.cleaned_data['user']
            login(request, user)
            return redirect('inicio')
    else:
        form = EmailLoginForm()
    return render(request, 'registration/login_email.html', {'form': form})

# Páginas informativas
def informacion(request):
    return render(request, 'informacion.html')

def servicios(request):
    return render(request, 'servicios.html')

def privacidad(request):
    return render(request, 'privacidad.html')

def envios(request):
    return render(request, 'envios.html')

def opinion(request):
    return render(request, 'opinion.html')

def pagos(request):
    return render(request, 'pagos.html')

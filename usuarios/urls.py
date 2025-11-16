from django.urls import path
from .views import (
    inicio, crear_cuenta, login_con_email,
    informacion, servicios, privacidad,
    envios, opinion, pagos
)

urlpatterns = [
    path('', inicio, name='inicio'),
    path('registro/', crear_cuenta, name='crear_cuenta'),
    path('login/', login_con_email, name='login'),
    path('informacion/', informacion, name='informacion'),
    path('servicios/', servicios, name='servicios'),
    path('privacidad/', privacidad, name='privacidad'),
    path('envios/', envios, name='envios'),
    path('opinion/', opinion, name='opinion'),
    path('pagos/', pagos, name='pagos'),
]


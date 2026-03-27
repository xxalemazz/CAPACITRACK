from django.urls import path
from . import views

urlpatterns = [

path('',views.login_view,name='login'),
path('registro/',views.registro,name='registro'),
path('dashboard/',views.dashboard,name='dashboard'),
path('productos/',views.productos,name='productos'),
path('pedido/',views.nuevo_pedido,name='pedido'),
path('pedidos/',views.pedidos,name='pedidos'),

]
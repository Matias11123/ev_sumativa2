from django.urls import path
from . import views

app_name = 'home' # Namespace (Punto 4 de la pauta)

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('genero/<str:genero_id>/', views.detalle_genero, name='detalle_genero'),
]
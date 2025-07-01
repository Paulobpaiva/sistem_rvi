from django.urls import path
from . import views

app_name = 'motoristas'

urlpatterns = [
    path('', views.motoristas_list, name='list'),
    path('novo/', views.motorista_create, name='create'),
    path('editar/<int:pk>/', views.motorista_update, name='update'),
    path('excluir/<int:pk>/', views.motorista_delete, name='delete'),
]

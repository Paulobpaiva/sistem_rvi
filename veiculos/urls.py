from django.urls import path
from . import views

app_name = 'veiculos'

urlpatterns = [
    path('', views.veiculos_list, name='list'),
    path('novo/', views.veiculo_create, name='create'),
    path('editar/<int:pk>/', views.veiculo_update, name='update'),
    path('excluir/<int:pk>/', views.veiculo_delete, name='delete'),
]

from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

app_name = 'solicitacoes'

router = DefaultRouter()
router.register(r'horarios-disponiveis', views.HorarioDisponivelViewSet)
router.register(r'solicitacoes', views.SolicitacaoViewSet)

urlpatterns = [
    path('', views.solicitacoes_list, name='list'),
    path('api/', include(router.urls)),
    path('solicitar/', views.solicitar_veiculo, name='solicitar'),
    path('solicitacao/<int:pk>/aprovar/', views.aprovar_solicitacao, name='aprovar'),
    path('solicitacao/<int:pk>/cancelar/', views.cancelar_solicitacao, name='cancelar'),
    path('horarios-livres/', views.horarios_livres, name='horarios_livres'),
]

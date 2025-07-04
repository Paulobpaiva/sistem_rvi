from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views
from solicitacoes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('motoristas/', include('motoristas.urls')),
    path('veiculos/', include('veiculos.urls')),
    path('solicitacoes/', include('solicitacoes.urls')),
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.home, name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

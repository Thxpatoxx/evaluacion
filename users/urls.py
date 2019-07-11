from django.urls import path
from .views import SignUpView
from . import views
from django.conf import settings # new
from django.urls import path, include # new
from django.conf.urls.static import static # new

urlpatterns = [
    path('signup/', SignUpView.as_view(), name='signup'),
    path('', views.encuestas, name='encuestas'),
    path('Informar', views.informar, name='informar'),
    path('Evento', views.evento, name='evento'),
    path('Respuestas/<int:pk>/', views.respuestas, name='respuestas'),
    path('NuevaRespuesta', views.nuevarespuesta, name='nuevarespuesta'),
    path('NuevoInforme', views.nuevoinforme, name='nuevoinforme'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
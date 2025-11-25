from django.urls import path, include
from rest_framework.routers import DefaultRouter
from admision_api.core.views.estudiante import EstudianteViewSet
from admision_api.core.views.instituto import InstitutoViewSet
from admision_api.core.views.carrera import CarreraViewSet
from admision_api.core.views.solicitud import SolicitudViewSet
from admision_api.core.views.resultado import ResultadoViewSet
from admision_api.core.views.auth import login_view, logout_view, register_view, user_profile_view

router = DefaultRouter()
router.register('estudiantes', EstudianteViewSet)
router.register('institutos', InstitutoViewSet)
router.register('carreras', CarreraViewSet)
router.register('solicitudes', SolicitudViewSet)
router.register('resultados', ResultadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/login/', login_view, name='login'),
    path('auth/logout/', logout_view, name='logout'),
    path('auth/register/', register_view, name='register'),
    path('auth/profile/', user_profile_view, name='user-profile'),
]

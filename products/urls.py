from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductViewSet
from django.conf.urls.static import static
from django.conf import settings

router = DefaultRouter()
router.register(r'products', ProductViewSet, basename='product')

urlpatterns = [
    path('api/v1/', include(router.urls)),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

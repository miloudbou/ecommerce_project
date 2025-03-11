from django.urls import path, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from products.views import ProductViewSet # type: ignore

router = DefaultRouter()
router.register(r'products', ProductViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls)),  # إضافة API المنتجات
]



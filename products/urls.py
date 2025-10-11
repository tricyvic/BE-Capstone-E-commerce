from rest_framework.routers import DefaultRouter
from .views import ProductViewSet, CategoryViewSet

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'', ProductViewSet)

urlpatterns = router.urls

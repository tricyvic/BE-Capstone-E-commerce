from django.shortcuts import render,redirect
from django.contrib import admin
from django.urls import path, include,re_path
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Ecom Watch API",
        default_version='v1',
        description="API documentation for the Ecom Watch backend.",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="support@ecomwatch.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)

def home(request):
    return render(request, 'index.html')

urlpatterns = [
    path('admin/', admin.site.urls),

    # JWT auth endpoints
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # App endpoints
    path('api/users/', include('users.urls')),
    path('api/products/', include('products.urls')),
    path('api/cart/', include('cart.urls')),
    path('api/orders/', include('orders.urls')),

    # Homepage
    path('', home, name='home'),  #soon

    # Swagger & ReDoc
     re_path(r'^swagger(?P<format>\.json|\.yaml)$',
            schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0),
         name='schema-redoc-ui'),

    # Optional: homepage
    path('', schema_view.with_ui('swagger', cache_timeout=0),
         name='api-docs-home'),
]

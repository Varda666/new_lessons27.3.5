from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/policies/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,

)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(('lms_service.urls', 'lms_service'), namespace='lms_service')),
    path('users/', include(('users.urls', 'users'), namespace='users')),
    path('drf-auth/', include(('rest_framework.urls',' rest_framework'), namespace='drf-auth')),
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

    ]


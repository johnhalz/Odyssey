from django.contrib import admin
from django.urls import path, include

from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path("api/hardware/", include("hardware.urls")),
    path("api/production/", include("production.urls")),
    path("api/testing/", include("testing.urls")),
    path("api/values/", include("values_and_units.urls")),
    path('api/accounts/', include('accounts.urls'))
]

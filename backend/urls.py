from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from lanternDie import views
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include(router.urls)),
    path("", include("lanternDie.urls")),
    path("accounts/", include("django.contrib.auth.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root = settings.STATIC_ROOT)

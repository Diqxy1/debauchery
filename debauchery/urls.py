from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from coachs.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('accounts.urls')),
    path('api/v2/', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
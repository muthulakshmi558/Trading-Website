from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('tradingapp.urls')),  # Include app URLs
]

# Serve media files in development only
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# Note: In production (DEBUG=False), static files and media files
# should be served via the web server or Render's static files configuration.

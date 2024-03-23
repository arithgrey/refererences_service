from django.contrib import admin
from django.views.static import serve
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    #path('admin/', admin.site.urls),
    path('api/business/', include('business.urls')),
    path('api/image/', include('image.urls')),
    path('uploads/<path:path>', serve, {'document_root': settings.MEDIA_ROOT}),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
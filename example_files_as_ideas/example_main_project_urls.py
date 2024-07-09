from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('diseases/', include('diseases.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

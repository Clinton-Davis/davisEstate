
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('listings/', include('listings.urls', namespace='listings')),
    path('accounts/', include('accounts.urls', namespace='accounts')),
    path('contact/', include('contact.urls', namespace='contacts')),
    path('admin/', admin.site.urls),
] 
if settings.DEBUG:

    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
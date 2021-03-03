
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('pages.urls', namespace='pages')),
    path('listings/', include('listings.urls', namespace='listings')),
    path('admin/', admin.site.urls),
]

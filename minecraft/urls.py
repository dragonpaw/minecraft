from django.conf.urls.static import static
from django.urls import path, include
from django.conf import settings

from django.contrib import admin
from . import views

admin.autodiscover()

urlpatterns = [
    path('admin/doc/', include('django.contrib.admindocs.urls')),
    path('admin/', admin.site.urls),
    path('items/', views.item_index, name='items'),
    path('item/<slug:slug>/', views.item_detail, name='item_detail'),
]

if settings.DEBUG and settings.MEDIA_ROOT:
    urlpatterns += static(settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT)


from django.contrib import admin
from django.urls import path, include
from p_library import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('p_library.urls', namespace='p_library')),
    path('accounts/', include('allauth.urls')),
    path('pub/', views.publisher),
    path('friend/', views.friends),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

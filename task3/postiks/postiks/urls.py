from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from postiks import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('postsapp.urls')),
    path('users/', include('usersapp.urls')),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler404 = 'postiks.views.error_404_view'
handler500 = 'postiks.views.error_500_view'

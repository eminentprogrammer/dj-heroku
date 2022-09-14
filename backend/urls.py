from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


from django.conf.urls import handler400, handler403, handler404, handler500
from apps.https import views

handler400 = views.handler400
handler403 = views.handler403
handler404 = views.handler404
handler500 = views.handler500


urlpatterns = [
    path('', include('frontend.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG == True:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


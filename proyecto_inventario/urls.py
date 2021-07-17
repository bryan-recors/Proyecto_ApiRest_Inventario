
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
#para redirigir a las urls de las apps
from django.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(('apps.productos.urls','productos'))),
    path('',include(('apps.proveedores.urls','proveedores'))),
    path('',include(('apps.ventas.urls','ventas'))),
    path('',include(('apps.compras.urls','compras'))),
    path('',include(('apps.users.urls','users'))),

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

from django.contrib import admin
from django.urls import path,include 
from shapeyourbot.apps.core.routing import websocket_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("shapeyourbot.apps.core.urls")),
    path('auth/', include("shapeyourbot.apps.authentication.urls"))
]

urlpatterns += websocket_urlpatterns
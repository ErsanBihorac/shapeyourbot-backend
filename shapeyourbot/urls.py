from django.contrib import admin
from django.urls import path,include 
from shapeyourbot.apps.core.routing import websocket_urlpatterns
<<<<<<< HEAD

urlpatterns = [
    path('admin/', admin.site.urls),
]
=======
from shapeyourbot.apps.core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include("shapeyourbot.apps.core.urls"))
]

>>>>>>> feat/rag
urlpatterns += websocket_urlpatterns
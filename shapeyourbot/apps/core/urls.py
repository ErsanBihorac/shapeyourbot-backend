<<<<<<< HEAD
from django.urls import path
from . import views

urlpatterns = [
    path("", views.lobby)
=======
from django.urls import path, include
from . import views
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r"documents", views.DocumentViewSet, basename="document")

urlpatterns = [
    path("", include(router.urls)),
>>>>>>> feat/rag
]
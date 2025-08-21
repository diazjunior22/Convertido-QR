from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
        path("descargar_qr/", views.descargar_qr, name="descargar_qr"),

]

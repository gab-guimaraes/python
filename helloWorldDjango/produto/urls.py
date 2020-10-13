from sys import path

from produto import views

urlpatterns = [
    path('', views.metodo)
]
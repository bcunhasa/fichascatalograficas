""" Define padrões de URL para o app Fichas """

from django.conf.urls import url

from . import views

urlpatterns = [
    # Página inicial
    url(r'^$', views.index, name='index'),
    url(r'^ficha/$', views.ficha, name='ficha'),
]

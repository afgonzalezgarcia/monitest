from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    url(r'^$', views.procesar_pedido, name='home_pedido'),
    #url(r'^setup/$', views.setup, name='setup'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
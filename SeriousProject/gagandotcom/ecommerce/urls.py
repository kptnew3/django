from django.conf.urls import url
from ecommerce import views, urls


urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^ecommerce/index/$', views.form_submitted, name='form_submitted'),
#    url(r'^ecommerce/ecommerce/index', views.form_submitted, name='form_submitted'),
]

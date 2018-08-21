from django.conf.urls import url
from helpapp import views

urlpatterns=[
    url(r'^$',views.funchelpapp,name="funchelpapp"),
]

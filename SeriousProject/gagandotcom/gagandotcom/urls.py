"""gagandotcom URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import url
from django.conf.urls import include
from ecommerce import urls
from ecommerce import views as ecomviews

print("hit the gagandotcom.urls")
urlpatterns = [
    url(r'^$', include('ecommerce.urls')),
#    url(r'^ecommerce/index/$',  ecomviews.form_submitted, name='form_submitted'),
    url(r'^ecommerce/index/', include('ecommerce.urls')),
    url(r'^admin/', admin.site.urls),
]


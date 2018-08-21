from django.conf.urls import url
from DjangoExerciseApp import views

urlpatterns = [
    url(r'^$',views.index1,name='index'),
]

from django.conf.urls import url
from adminpage import views

urlpatterns = [
    url(r'^$', views.adminhome),
]
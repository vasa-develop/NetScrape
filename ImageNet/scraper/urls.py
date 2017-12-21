from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^imagescraper/scrape', views.index ,name="index"),
    url(r'^imagescraper' , views.imagescraper , name="imagescraper"),
]
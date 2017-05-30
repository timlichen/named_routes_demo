from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^(?P<schmoo>\d+)$', views.index, name="index"),
    url(r'^post_test$', views.post_test, name="post_test"),
]

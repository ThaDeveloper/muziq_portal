from django.conf.urls import url
from . import views

urlpatterns = [
    # index references /music/ url pattern
    url(r'^$', views.index, name = 'index'),

    # /music/712/
    url(r'^(?P<album_id>[0-9]+)/$', views.detail, name = 'detail'),
]
from django.conf.urls import url
from . import views

urlpatterns = [
    #url(r'^$', views.post_list, name='post_list'),

    url(r'^$', views.index, name='index'),

    url(r'analsys', views.analsys, name='analsys'),

    url(r'rank', views.rank, name='rank'),
]
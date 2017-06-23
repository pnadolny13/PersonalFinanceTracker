from django.conf.urls import url
from . import views

urlpatterns = [
    #/budget/
    url(r'^$', views.index, name='index'),
    # /budget/71/
    url(r'^(?P<budget_id>[0-9]+)/$', views.detail, name='detail'),
    # /budget/June/
    url(r'^(?P<month_id>[\w\-]+)/$', views.months, name='months'),
]
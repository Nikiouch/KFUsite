from django.conf.urls import url, include
from . import views

urlpatterns = [
		url(r'^(?P<ID>[0-9]+)/$', views.office, name='office'),
		url(r'^(?P<ID>[0-9]+)/work/$', views.work, name='work'),
		url(r'^(?P<ID>[0-9]+)/member/$', views.member, name='member'),
		url(r'^(?P<ID>[0-9]+)/director/$', views.director, name='director'),
		url(r'^(?P<ID>[0-9]+)/organization/$', views.organization, name='organization'),
		url(r'^(?P<ID>[0-9]+)/receipt/$', views.receipt, name='receipt'),
]
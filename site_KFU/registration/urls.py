from django.conf.urls import url, include
from registration import views


urlpatterns = [
    url(r'^', views.work_registration, name='work'),
    url(r'^work', views.work_registration, name='work'),
    url(r'^organization/(?P<workid>[0-9]+)', views.org_registration, name='org_registration'),
    url(r'^member/(?P<directormemberID>[0-9]+)/(?P<orgID>[0-9]+)/$', views.member_registration, name='member_registration'),
    url(r'^director/(?P<directormemberID>[0-9]+)/$', views.director_registration, name='director_registration'),
    url(r'^finale', views.finale, name='finale'),
    url(r'^login', include('login.urls')),
]

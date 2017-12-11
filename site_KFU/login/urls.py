from django.conf.urls import url, include
from login import views


urlpatterns = [
		url(r'^$', views.log_in, name="log_in"),
		url(r'^office', include('office.urls')),
]
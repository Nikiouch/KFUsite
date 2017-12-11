from django.conf.urls import url, include
from buffet import views

urlpatterns = [
		url(r'^$', views.registration, name="registration"),
]
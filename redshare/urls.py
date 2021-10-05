from django.urls import path

from . import views

urlpatterns = [
	path("", views.redshare),
	path("display/", views.display),
	path("login", views.login),
	path("signup", views.signup),
	path("add-donor", views.add_donor),
	path("logout", views.logout)
]
from django.urls import path

from . import views

urlpatterns = [
    path("", views.HomeView.as_view(), name="statshome"),
    path("b", views.BatterView.as_view(), name="batters"),
    path("p", views.PitcherView.as_view(), name="pitchers")
]
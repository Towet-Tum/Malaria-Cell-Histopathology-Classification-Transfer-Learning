from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("train_model/", views.train_model, name="train_model"),
    path("upload/", views.upload, name="upload"),
    path("results/", views.results, name="results"),
    path("dashboard/", views.dashboard, name="dashboard"),
]

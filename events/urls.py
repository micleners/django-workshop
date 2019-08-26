from django.urls import path
from . import views

app_name = "events"
urlpatterns = [
    path("", views.listTemplateView, name="list"),
    path("create", views.createTemplateView, name="create"),
    path("add", views.EventCreateView.as_view(), name="add"),
    path("delete", views.EventDeleteView.as_view(), name="delete"),
]

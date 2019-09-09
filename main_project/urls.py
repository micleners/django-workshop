from django.urls import include, path
from django.contrib import admin
from rest_framework import routers
from events import views

router = routers.DefaultRouter()
router.register(r"users", views.UserViewSet)
router.register(r"events", views.EventViewSet)

urlpatterns = [
    path("api/", include(router.urls)),
    path("admin/", admin.site.urls),
    path("events/", include("events.urls")),
]

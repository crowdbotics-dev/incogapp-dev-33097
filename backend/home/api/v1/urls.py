from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import Cvdd123ViewSet, SghjtViewSet

from home.api.v1.viewsets import (
    SignupViewSet,
    LoginViewSet,
)

router = DefaultRouter()
router.register("signup", SignupViewSet, basename="signup")
router.register("login", LoginViewSet, basename="login")
router.register("sghjt", SghjtViewSet)
router.register("cvdd123", Cvdd123ViewSet)

urlpatterns = [
    path("", include(router.urls)),
]

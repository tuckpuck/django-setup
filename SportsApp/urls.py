from django.urls import path
from .views import Sports

urlpatterns = [
    path('sports/', Sports, name="sports"),
]
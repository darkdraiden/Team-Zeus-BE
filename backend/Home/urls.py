from django.urls import path
from Home.views import UserView


urlpatterns = [
    path("",UserView.as_view())
]
from django.urls import path
from Home.views import UserView,UserLoginView


urlpatterns = [
    path("",UserView.as_view()), #for signup page 
    path("<str:user_name>",UserLoginView.as_view()) #for login page 
]
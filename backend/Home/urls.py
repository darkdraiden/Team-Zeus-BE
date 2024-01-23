from django.urls import path
from Home.views import UserView,UserLoginView,AddUsertoBoard,AddTaskView,AddBoardView,BoardDetailsView


urlpatterns = [
    path("",UserView.as_view()), #for signup page 
    path("<str:user_name>",UserLoginView.as_view()), #for login page 
    path("<str:user_name>/dashboard",UserLoginView.as_view()), #for login page 
    path("<str:user_name>/<int:board_id>",AddUsertoBoard.as_view()), #add user to board
    path("<str:user_name>/<int:board_id>/addtask",AddTaskView.as_view()), #add task to board
    path("<str:user_name>/addboard",AddBoardView.as_view()), #add new board
    path("<str:board_id>",BoardDetailsView.as_view())
]


from rest_framework import status
from rest_framework.views import APIView,Response
from Home.models import User,Board,Task,UserBoard
from Home.serializers import UserSerializer

# Create your views here.
class UserView(APIView):
    def post(self,request):
        response={}
        if 'user_name' not in request.data:
            response['success']=False
            response['message']="Name required"
            return Response(response,status.HTTP_400_BAD_REQUEST)
        user_name=request.data['user_name'].replace(" ", "")
        first_name=request.data['first_name'].replace(" ", "")
        last_name=request.data['last_name'].replace(" ", "")
        user_email=request.data['user_email'].replace(" ", "")
        password=request.data['password']
        User.objects.create(user_email=user_email,user_name=user_name,first_name=first_name,password=password,last_name=last_name)
        response={
            "success": True,
            "message": "User added successfully"
        }
        return Response(response,status.HTTP_200_OK)
    
class UserLoginView(APIView):
    def post(self,request,user_name):
        print("in userloginview")
        response={}
        if 'user_name' not in request.data:
            response['success']=False
            response['message']='user name required'
            return Response(response,status.HTTP_400_BAD_REQUEST)
        user_name=request.data['user_name']
        password=request.data['password']
        user=User.objects.filter(user_name=user_name).first()
        if not user:
            return Response(response,status.HTTP_401_UNAUTHORIZED)
        if user_name==user.user_name and password==user.password:
            board=Board.objects.all()
            list=[]
            for i in board:
                dict={
                    "board_id":i.board_id,
                    "board_name":i.board_name,
                }
                list.append(dict)
            data={
                "user_name": user_name,
                "boards": list
            }
            response={
            "success": True,
            "message": "User successfully authenticated",
            "data": data,
        }   
            return Response(response,status.HTTP_200_OK)
        else:
            response={
            "success": False,
            "message": "Invalid credentials",
        }
            return Response(response,status.HTTP_401_UNAUTHORIZED)
    
    def get(self,request,user_name):
        board=Board.objects.all()
        list=[]
        for i in board:
            dict={
                "board_id":i.board_id,
                "board_name":i.board_name,
            }
            list.append(dict)
        data={
            "user_name": user_name,
            "boards": list
        }
        response={
        "success": True,
        "message": "User and board details send successfully",
        "data": data,
    }   
        return Response(response,status.HTTP_200_OK)

class AddUsertoBoard(APIView):
    def post(self,request,user_name,board_id):
        response={}
        user_id=User.objects.filter(user_name=user_name).first().user_id
        UserBoard.objects.create(user_id=user_id,board_id=board_id)
        list=[]
        board=Board.objects.all()
        for i in board:
                dict={
                    "board_id":i.board_id,
                    "board_name":i.board_name,
                }
                list.append(dict)
        data={
                "user_name": user_name,
                "boards": list
            }
        response={
            "success": True,
            "message": "User joined board",
            "data":data
        }
        return Response(response,status.HTTP_200_OK)

class AddTaskView(APIView):
    def post(self,request,user_name,board_id):
        response={}
        if 'task_name' not in request.data:
            response['success']=False
            response['message']="Need task name"
            return Response(response,status.HTTP_400_BAD_REQUEST)
        task_name=request.data['task_name'].replace(" ", "")
        task_desc=request.data['task_desc']
        task_status=request.data['task_status']
        Task.objects.create(task_name=task_name,task_desc=task_desc,task_status=task_status,board_id=board_id)
        list=[]
        board=Board.objects.all()
        for i in board:
                dict={
                    "board_id":i.board_id,
                    "board_name":i.board_name,
                }
                list.append(dict)
        data={
                "user_name": user_name,
                "boards": list
            }
        response={
            "success": True,
            "message": "User joined board",
            "data":data
        }
        return Response(response,status.HTTP_200_OK)
        
class AddBoardView(APIView):
    def post(self,request,user_name):
        response={}
        if 'board_name' not in request.data:
            response['success']=False
            response['message']="Need board name"
        board_name=request.data['board_name']
        Board.objects.create(board_name=board_name)
        list=[]
        board=Board.objects.all()
        for i in board:
                dict={
                    "board_id":i.board_id,
                    "board_name":i.board_name,
                }
                list.append(dict)
        data={
                "user_name": user_name,
                "boards": list
            }
        response={
            "success": True,
            "message": "Board added successfully",
            "data": data

        }
        return Response(response,status.HTTP_200_OK)

class BoardDetailsView(APIView):
     def post(self,request,board_id):
          pass
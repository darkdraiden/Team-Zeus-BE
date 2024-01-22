from rest_framework import status
from rest_framework.views import APIView,Response
from Home.models import User
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
                response={
                "success": True,
                "message": "User successfully authenticated",
            }
                return Response(response,status.HTTP_200_OK)
            else:
                response={
                "success": False,
                "message": "Invalid credentials",
            }
                return Response(response,status.HTTP_401_UNAUTHORIZED)

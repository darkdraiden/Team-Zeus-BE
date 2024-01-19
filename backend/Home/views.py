from rest_framework import status
from rest_framework.views import APIView,Response
from Home.models import User
from Home.serializers import UserSerializer

# Create your views here.
class UserView(APIView):
    def post(self,request):
        response={
            "success": True,
            "message": "User Added "
        }
        if 'user_name' not in request.data:
            response['success']=False
            response['message']='name required'
            return Response(response,status.HTTP_400_BAD_REQUEST)
        user_name=request.data['user_name']
        first_name=request.data['first_name']
        last_name=request.data['last_name']
        user_email=request.data['user_email']
        password=request.data['password']
        User.objects.create(user_email=user_email,user_name=user_name,first_name=first_name,password=password,last_name=last_name)
        return Response(response,status.HTTP_200_OK)
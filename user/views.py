from rest_framework.views import APIView,Request,Response,status
from rest_framework import generics
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate
from rest_framework.authentication import TokenAuthentication
from .permissions import UsePatchRotePermition, UsePatchRotePermitionDetail
from .serializers import AccountSerializer, LoginSerializer, SellerProductSerializer
from .models import User
# Create your views here.

class UserView(generics.ListCreateAPIView):
    serializer_class = AccountSerializer
    queryset = User.objects.all()
        


class UserViewDetail(generics.ListAPIView):
        serializer_class = AccountSerializer
        queryset = User.objects.all()
        
        def get_queryset(self):
             num=self.kwargs["num"]
             return self.queryset.order_by("-date_joined")[0:num]

class UserViewDetailEdit(generics.UpdateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[UsePatchRotePermition]
    queryset = User.objects.all()
    serializer_class= SellerProductSerializer
    
    
class UserViewDetailDelete(generics.UpdateAPIView):
    authentication_classes=[TokenAuthentication]
    permission_classes=[UsePatchRotePermitionDetail]
    queryset = User.objects.all()
    serializer_class= SellerProductSerializer
               

class LoginView(APIView):
    def post(self, request:Request):
        serializer= LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        user = authenticate(**serializer.validated_data)

        if not user:
            return Response({"detail": "invalid credentials"}, status.HTTP_403_FORBIDDEN)
            
        token,created= Token.objects.get_or_create(user=user)
        return Response({"token":token.key})
            
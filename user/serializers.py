
from rest_framework import serializers
from user.models import User


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields=["username","first_name","last_name","is_seller","date_joined","is_active","is_superuser","password"]
        extra_kwargs = {'is_seller': {'required': True},'password': {'required': True,'write_only': True}}

    def create(self,validated_data):
        user=User.objects.create_user(**validated_data)
        return user
    
    
class SellerProductSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        fields=["id","username","first_name","last_name","is_seller","date_joined","is_active","is_superuser"]    

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(write_only=True)
    password = serializers.CharField(write_only=True)        
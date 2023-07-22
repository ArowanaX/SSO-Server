from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.password_validation import validate_password


User = get_user_model()



class PublicUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('id', 'email','first_name', 'last_name')


class UserSerializer(serializers.ModelSerializer):

    is_sso_admin = serializers.ReadOnlyField(source='is_staff')

    class Meta:
        model = User
        fields = ('id','email','first_name', 'last_name','is_sso_admin',)


class CreateUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('email','first_name', 'last_name', 'password')

    def validate_password(self, value):
        validate_password(value)
        return value

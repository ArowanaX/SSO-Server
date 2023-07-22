from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.permissions import IsOwner
from user.serializers import CreateUserSerializer, UserSerializer,PublicUserSerializer

User = get_user_model()


class ListAllUsersAPIView(ListAPIView):
    serializer_class = PublicUserSerializer

    def get_queryset(self):
        request_user = self.request.user
        return User.objects.exclude(id=request_user.id)


class UserProfileView(RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated, IsOwner,)
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_object(self):
        return self.request.user


class UserSignUpView(APIView):

    def post(self, request, *args, **kwargs):
        serialized = CreateUserSerializer(data=request.data)
        if serialized.is_valid():
            serializer_data = serialized.validated_data
            User.objects.create_user(**serializer_data)
            serializer_data = serialized.data
            serializer_data.pop('password')
            return Response(serializer_data, status=status.HTTP_201_CREATED)
        else:
            return Response(serialized.errors, status=status.HTTP_400_BAD_REQUEST)

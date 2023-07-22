from django.conf import settings
from django.contrib.auth import get_user_model
from rest_framework.generics import ListCreateAPIView, RetrieveDestroyAPIView,CreateAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from user.permissions import IsSSOAdminOrReadOnly
from .models import Service, Connection
from .serializers import ServiceSerializer, ConnectionSerializer,PublicServiceSerializer

User = get_user_model()
PUBLIC_KEY = open(settings.JWT_PUBLIC_KEY_PATH).read()


class FetchPublicKeyAPIView(APIView):

    def get(self, request):
        return Response({'key': PUBLIC_KEY})



class ListCreateServiceAPIView(ListCreateAPIView):
    permission_classes = (IsAuthenticated, IsSSOAdminOrReadOnly,)
    queryset = Service.objects.all()


    def get_serializer_class(self):
        ser = {
            'GET': PublicServiceSerializer,
            'POST': ServiceSerializer
        }
        return ser[self.request.method]


class CreateConnectionAPIView(CreateAPIView):
    serializer_class = ConnectionSerializer
    permission_classes = (IsAuthenticated, IsSSOAdminOrReadOnly)



class ConnectionDetailAPIView(RetrieveDestroyAPIView):
    serializer_class = ConnectionSerializer
    permission_classes = (IsAuthenticated, IsSSOAdminOrReadOnly)
    queryset = Connection.objects.all()

from django.urls import path
from .views import ListCreateServiceAPIView, CreateConnectionAPIView,FetchPublicKeyAPIView,ConnectionDetailAPIView


app_name = 'service'

urlpatterns = [
    path('fetch-public-key/', FetchPublicKeyAPIView.as_view(), name='fetch-public-key'),

    path('service/', ListCreateServiceAPIView.as_view(), name='list-create-service'),

    path('connection/new/', CreateConnectionAPIView.as_view(), name='create-connection'),
    path('connection/<int:pk>/', ConnectionDetailAPIView.as_view(), name='connection-detail'),
]

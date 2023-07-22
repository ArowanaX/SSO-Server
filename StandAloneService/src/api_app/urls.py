from django.urls import path
from api_app import views

app_name = 'api_app'

urlpatterns = [
    path('protected-resource/', views.ProtectedDataAPIView.as_view(), name='fetch-protected-resource'),
]

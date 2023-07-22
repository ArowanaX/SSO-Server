from user.views import UserSignUpView, UserProfileView, ListAllUsersAPIView
from django.urls import path

app_name = 'users'

urlpatterns = [
    path('signup/', UserSignUpView.as_view(), name='signup-api'),
    path('user/', UserProfileView.as_view(), name='user-retrieve-update-destroy-api'),
    path('users/all/', ListAllUsersAPIView.as_view(), name='list-all-users-api'),
]

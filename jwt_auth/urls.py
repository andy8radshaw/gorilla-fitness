from django.urls import path
from .views import RegisterView, LoginView, ProfileListView, ProfileDetailView, MyProfileView

urlpatterns = [
    path('register/', RegisterView.as_view()),
    path('login/', LoginView.as_view()),
    path('users/', ProfileListView.as_view()),
    path('users/<username>/', ProfileDetailView.as_view()),
    path('myprofile/', MyProfileView.as_view()),
]
from django.urls import path
from .views import WorkoutGroupListView, WorkoutGroupDetailView

urlpatterns = [
    path('', WorkoutGroupListView.as_view()),
    path('<int:pk>/', WorkoutGroupDetailView.as_view())
]
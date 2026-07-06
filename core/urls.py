from django.urls import path
from .views import home, JobListAPI, UserTestAPI, JobCreateAPI

urlpatterns = [
    path('', home),
    path('joblist/', JobListAPI.as_view()),
    path('usertest/', UserTestAPI.as_view()),
    path('jobcreate/', JobCreateAPI.as_view()),
]
from django.urls import path
from .views import home, JobListAPI, UserTestAPI, JobCreateAPI, SignupAPI

urlpatterns = [
    path('', home),
    path('joblist/', JobListAPI.as_view()),
    path('usertest/', UserTestAPI.as_view()),
    path('jobcreate/', JobCreateAPI.as_view()),
    path('signup/', SignupAPI.as_view()),
]
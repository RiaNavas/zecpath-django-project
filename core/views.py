from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job
from .serializers import JobSerializer, UserSignupSerializer

def home(request):
    return HttpResponse("Hello Zecpath Backend")


class JobListAPI(APIView):
    def get(self, request):
        jobs = Job.objects.all()
        serializer = JobSerializer(jobs, many=True)
        return Response(serializer.data)
    
class UserTestAPI(APIView):

    permission_classes = [IsAuthenticated]

    def get(self, request):
        return Response({
            "message": "User API Working",
            "user": str(request.user)
        })
    
class JobCreateAPI(APIView):
    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
class SignupAPI(APIView):

    def post(self, request):

        serializer = UserSignupSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
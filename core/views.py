from rest_framework.permissions import IsAuthenticated
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Job,CandidateProfile,EmployerProfile
from .serializers import JobSerializer, UserSignupSerializer, ApplicationSerializer, CandidateProfileSerializer, EmployerProfileSerializer
from .permissions import IsAdmin, IsEmployer, IsCandidate
from rest_framework.parsers import MultiPartParser

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

    permission_classes = [IsEmployer]

    def post(self, request):
        serializer = JobSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
class ApplyJobAPI(APIView):

    permission_classes = [IsCandidate]

    def post(self, request):

        serializer = ApplicationSerializer(
            data=request.data
        )

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
    
class AdminDashboardAPI(APIView):

    permission_classes = [IsAdmin]

    def get(self, request):
        return Response({
            "message": "Admin Access Granted"
        })
class CandidateProfileAPI(APIView):

    permission_classes = [IsCandidate]

    def post(self, request):

        serializer = CandidateProfileSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    
    def get(self, request):

        profile = CandidateProfile.objects.get(
        user=request.user
        )

        serializer = CandidateProfileSerializer(
        profile
        )

        return Response(serializer.data)
    
    def put(self, request):

        profile = CandidateProfile.objects.get(
            user=request.user
        )

        serializer = CandidateProfileSerializer(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    def delete(self, request):

        profile = CandidateProfile.objects.get(
        user=request.user
        )

        profile.is_deleted = True
        profile.save()

        return Response({
        "message": "Candidate profile deleted"
        })

class EmployerProfileAPI(APIView):

    permission_classes = [IsEmployer]

    def post(self, request):

        serializer = EmployerProfileSerializer(
            data=request.data
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)
    def get(self, request):

        profile = EmployerProfile.objects.get(
        user=request.user
        )

        serializer = EmployerProfileSerializer(
        profile
        )

        return Response(serializer.data)
    def put(self, request):

        profile = EmployerProfile.objects.get(
            user=request.user
        )

        serializer = EmployerProfileSerializer(
            profile,
            data=request.data,
            partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

        return Response(serializer.errors)

    def delete(self, request):

        profile = EmployerProfile.objects.get(
            user=request.user
        )

        profile.is_deleted = True
        profile.save()

        return Response({
            "message": "Employer profile deleted"
        })
class ResumeUploadAPI(APIView):

    permission_classes = [IsCandidate]
    parser_classes = [MultiPartParser]

    def post(self, request):

        profile = CandidateProfile.objects.get(
            user=request.user
        )

        resume = request.FILES.get(
            'resume'
        )

        if not resume:

            return Response({
                "message": "Resume file is required"
            })

        allowed_extensions = [
            '.pdf',
            '.doc',
            '.docx'
        ]

        filename = resume.name.lower()

        if not any(
            filename.endswith(ext)
            for ext in allowed_extensions
        ):

            return Response({
                "message": "Only PDF, DOC and DOCX files are allowed"
            })

        max_size = 5 * 1024 * 1024

        if resume.size > max_size:

            return Response({
                "message": "File size exceeds 5MB"
            })

        profile.resume = resume

        profile.save()

        return Response({
            "message": "Resume uploaded successfully",
            "resume": profile.resume.url
        })
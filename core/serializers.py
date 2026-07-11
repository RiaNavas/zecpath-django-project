from rest_framework import serializers
from .models import Job, User
from .models import Application
from .models import CandidateProfile, EmployerProfile


class JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Job
        fields = '__all__'


class UserSignupSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'email',
            'phone',
            'role',
            'password'
        ]

        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        return User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            phone=validated_data.get('phone', ''),
            role=validated_data.get('role', 'Candidate')
        )
class ApplicationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Application
        fields = '__all__'

class CandidateProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = CandidateProfile

        fields = [
            'id',
            'user',
            'skills',
            'education',
            'experience',
            'expected_salary',
            'resume'
        ]
class EmployerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = EmployerProfile

        fields = [
            'id',
            'user',
            'company_name',
            'domain',
            'company_size',
            'is_verified'
        ]
from rest_framework import serializers
from .models import Student, Job, Candidate, JobApplication


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('pk', 'name', 'email', 'document', 'phone', 'registrationDate')


class JobSerializer(serializers.ModelSerializer):

    class Meta:
        model = Job
        fields = ('pk', 'name', 'total_applied', 'publishedDate')


class CandidateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Candidate
        fields = ('pk', 'name', 'phone', 'registrationDate')


class JobApplySerializer(serializers.ModelSerializer):

    class Meta:
        model = JobApplication
        fields = ('pk', 'candidate', 'job')

from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

# Create your views here.
class all_subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(Subject.objects.all(), many = True)
        return Response(subjects.data)
    
class a_subject(APIView):
    def get(self, request, subject):
        subject = get_object_or_404(Subject, subject_name__iexact=subject)
        return Response(SubjectSerializer(subject).data)
from .models import Subject
from .serializers import SubjectSerializer
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.
class all_subjects(APIView):
    def get(self, request):
        subjects = SubjectSerializer(Subject.objects.all(), many = True)
        return Response(subjects.data)
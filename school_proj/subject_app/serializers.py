from rest_framework.serializers import ModelSerializer, SerializerMethodField
from django.db.models import Avg
from .models import Subject

class SubjectSerializer(ModelSerializer):
    students = SerializerMethodField()
    grade_average = SerializerMethodField()

    class Meta:
        model = Subject
        fields = ['subject_name', 'professor', 'students', 'grade_average']

    def get_students(self, obj):
        return obj.student.count()  

    def get_grade_average(self, obj):
        return round(obj.grade.aggregate(avg=Avg('grade'))['avg'] or 0, 2)

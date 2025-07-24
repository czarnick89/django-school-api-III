from django.db import models
from student_app.models import Student
from .validators import *
#from django.core.exceptions import ValidationError

# Create your models here.
class Subject(models.Model):
    subject_name = models.CharField(null=False, blank=False, unique=True, validators=[validate_title_case])
    professor = models.CharField(null=False, blank=False, default='Mr. Cahan', validators=[validate_professor_name])
    students = models.ManyToManyField(Student, related_name='subject') 

    def __str__(self):
        return f"{self.subject_name} - {self.professor} - {self.students.count()}" 

    def add_a_student(self, student_id):
        if self.students.count()<30:
            self.students.add(student_id)
        else:
            raise Exception("This subject is full!")

    def drop_a_student(self, student_id):
        if self.students.count() >0:
            self.students.remove(student_id)
        else:
            raise Exception("This subject is empty!")

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from subject_app.models import Subject
from student_app.models import Student

# Create your models here.
class Grade(models.Model):
    grade = models.DecimalField(null=False, max_digits=5, decimal_places=2, validators=[MinValueValidator(0.00), MaxValueValidator(100.00)], default=100)
    a_subject = models.ForeignKey(Subject, related_name='grade', on_delete=models.CASCADE)
    student = models.ForeignKey(Student, related_name='grade', on_delete=models.CASCADE)
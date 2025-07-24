from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from .validators import *
#from django.core.exceptions import ValidationError

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100, null=False, blank=False, validators=[validate_name_format]) 
    student_email = models.EmailField(max_length=100, null=False, blank=False, unique=True, validators=[validate_school_email])
    personal_email = models.EmailField(max_length=100, blank=True, null=True, unique=True)
    locker_number = models.IntegerField(null=False, blank=False, unique=True, default=110, validators=[MinValueValidator(1), MaxValueValidator(200)])
    locker_combination = models.CharField(max_length=20, null=False, blank=False, default="12-12-12", validators=[validate_combination_format])
    good_student = models.BooleanField(null=False, default=True)
    subjects = models.ManyToManyField('subject_app.Subject', related_name='student')

    def __str__(self):
        return f"{self.name} - {self.student_email} - {self.locker_number}"
    
    def locker_reassignment(self, number):
        self.locker_number = number
        self.save()

    def student_status(self, status):
        self.good_student = status
        self.save()

    def add_subject(self, subject_id):
        if self.subjects.count()<7:
            self.subjects.add(subject_id)
        else:
            raise Exception("This students class schedule is full!")
        
    def remove_subject(self, subject_id):
        if self.subjects.count() > 0:
            self.subjects.remove(subject_id)
        else:
            raise Exception("This students class schedule is empty!")
from django.urls import path
from .views import all_students, a_student

urlpatterns = [
    path('', all_students.as_view(), name='all_students'),
    path('<int:id>/', a_student.as_view(), name='a_student')
]
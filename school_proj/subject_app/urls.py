from django.urls import path
from .views import all_subjects, a_subject

urlpatterns = [
    path('', all_subjects.as_view(), name='all_subjects'),
    path('<str:subject>/', a_subject.as_view(), name='a_subject')
]
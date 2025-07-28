from django.urls import path
from .views import all_subjects

urlpatterns = [
    path('', all_subjects.as_view(), name='all_subjects')
]
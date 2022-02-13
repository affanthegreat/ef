from django.urls import path
from .views import Demo

urlpatterns = [
    path('assignments/', Demo.as_view(), name='teacher-assignments')
]

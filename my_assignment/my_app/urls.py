from django.urls import path
from .views import assignment_signal

urlpatterns=[
    path('assignment_sample/',assignment_signal,name='assignment-sample')
]
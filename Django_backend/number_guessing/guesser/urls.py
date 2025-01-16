from django.urls import path
from . import views

urlpatterns = [
    path('guess/', views.guess_number),
]

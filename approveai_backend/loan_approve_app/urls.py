from django.urls import path
from .views import LoanPrediction 

urlpatterns = [
    path("loan", LoanPrediction),
]

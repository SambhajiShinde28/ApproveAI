from django.db import models

# Create your models here.
class LoanPredictionModel(models.Model):
    FullName = models.CharField(max_length=500, default="None")
    Address = models.CharField(max_length=600, default="None")
    Gender = models.CharField(max_length=100, default="None")
    Married = models.CharField(max_length=100, default="None")
    Dependence = models.CharField(max_length=100, default="None")
    Education = models.CharField(max_length=100, default="None")
    SelfEmployee = models.CharField(max_length=100, default="None")
    ApplicantIncome = models.IntegerField(default=0)
    CoapplicantIncome = models.IntegerField(default=0)
    LoanAmount = models.IntegerField(default=0)
    Loan_Amount_Term = models.IntegerField(default=0)
    Credit_History = models.IntegerField(default=0)
    PropertyArea = models.CharField(max_length=100, default="None")
    RejectedPercent = models.IntegerField(default=0)
    ApprovedPercent = models.IntegerField(default=0)
    ModelPrediction = models.IntegerField(default=0)
    LoanStatus = models.CharField(max_length=100, default="None")



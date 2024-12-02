from django.contrib import admin
from .models import LoanPredictionModel

# Register your models here.
class Loan_Prediction_Admin(admin.ModelAdmin):
    list_display = ('FullName', 'Address', 'Gender', 'Married', 'Dependence', 'Education', 'SelfEmployee', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History', 'PropertyArea', 'RejectedPercent', 'ApprovedPercent', 'ModelPrediction', 'LoanStatus')

admin.site.register(LoanPredictionModel,Loan_Prediction_Admin)
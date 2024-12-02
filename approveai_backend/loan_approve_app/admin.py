from django.contrib import admin
from .models import LoanPredictionModel

# Register your models here.
class Loan_Prediction_Admin(admin.ModelAdmin):
    list_display = ('FullName', 'Address', 'Gender', 'Married', 'Dependence', 'Education', 'SelfEmployee', 'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'LoanAmountTerm', 'CreditHistory', 'PropertyArea', 'RejectedPercentage', 'ApprovedPercentage', 'ModelPrediction', 'LoanStatus')

admin.site.register(LoanPredictionModel,Loan_Prediction_Admin)
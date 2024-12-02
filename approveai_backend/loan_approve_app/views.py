from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LoanPredictionModel
import json
import pandas as pd


@csrf_exempt
def LoanPrediction(req):

    if req.method == "POST":

        data = json.load(req)

        fullName=data["FullName"]
        address=data["Address"]
        gender=data['Gender']
        married=data['Married']
        dependents=data['Dependents']
        education=data['Education']
        selfEmployed=data['SelfEmployed']
        applicantIncome=data['ApplicantIncome']
        coapplicantIncome=data['CoapplicantIncome']
        loanAmount=data['LoanAmount']
        loanAmountTerm=data['LoanAmountTerm']
        creditHistory=data['CreditHistory']
        propertyArea=data['PropertyArea']

        # print(f"Model PRediction : {fullName} {address} {gender} {married} {dependents} {education} {selfEmployed} {applicantIncome} {coapplicantIncome} {loanAmount} {loanAmountTerm} {creditHistory} {propertyArea}")

        if fullName != "" and address != "" and gender != "" and married != "" and dependents != "" and education != "" and selfEmployed != "" and applicantIncome != "" and coapplicantIncome != "" and loanAmount != "" and loanAmountTerm != "" and creditHistory != "" and propertyArea != "":
            
            manual_data = {
                'Gender': 'Male',
                'Married': 'Yes',
                'Dependents': '1',
                'Education': 'Graduate',
                'Self_Employed': 'No',
                'ApplicantIncome': 5000,
                'CoapplicantIncome': 1500,
                'LoanAmount': 200,
                'Loan_Amount_Term': 360,
                'Credit_History': 1.0,
                'Property_Area': 'Urban'
            }

        else:
            return JsonResponse({"message":"fields empty"})

        return JsonResponse({"message":"This is post request"})
    else:
        return JsonResponse({"message":"False"})
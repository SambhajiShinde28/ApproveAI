from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LoanPredictionModel
import json


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
            pass

        else:
            return JsonResponse({"message":"fields empty"})

        return JsonResponse({"message":"This is post request"})
    else:
        return JsonResponse({"message":"False"})
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import LoanPredictionModel
import json
import pandas as pd
import joblib
import numpy as np
import os
from django.conf import settings
import sklearn

model_path=os.path.join(settings.BASE_DIR,'ML-Model/LoanPrediction_SVM_Model.pkl')
dencoding_path=os.path.join(settings.BASE_DIR,'ML-Model/DataEncodingFile_ScalarFile.pkl')
feature_columns_path = os.path.join(settings.BASE_DIR, 'ML-Model/feature_columns.pkl')

svm_model = joblib.load(model_path)
scaler = joblib.load(dencoding_path)
feature_columns = joblib.load(feature_columns_path)


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


        if fullName != "" and address != "" and gender != "" and married != "" and dependents != "" and education != "" and selfEmployed != "" and applicantIncome != "" and coapplicantIncome != "" and loanAmount != "" and loanAmountTerm != "" and creditHistory != "" and propertyArea != "":
            
            userData = {
                'Gender': gender,
                'Married': married,
                'Dependents': dependents,
                'Education': education,
                'Self_Employed': selfEmployed,
                'ApplicantIncome': int(applicantIncome),
                'CoapplicantIncome': int(coapplicantIncome),
                'LoanAmount': int(loanAmount),
                'Loan_Amount_Term': int(loanAmountTerm),
                'Credit_History': int(creditHistory),
                'Property_Area': propertyArea
            }

            manual_df = pd.DataFrame([userData])

            manual_df['Gender'] = manual_df['Gender'].map({'Male': 1, 'Female': 0})
            manual_df['Married'] = manual_df['Married'].map({'Yes': 1, 'No': 0})
            manual_df['Education'] = manual_df['Education'].map({'Graduate': 1, 'Not Graduate': 0})
            manual_df['Self_Employed'] = manual_df['Self_Employed'].map({'Yes': 1, 'No': 0})

            manual_df = pd.get_dummies(manual_df, columns=['Dependents', 'Property_Area'], drop_first=True)

            manual_df = manual_df.reindex(columns=feature_columns.columns, fill_value=0)

            numerical_cols = ['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term', 'Credit_History']
            manual_df[numerical_cols] = scaler.transform(manual_df[numerical_cols])

            manual_prediction = svm_model.predict(manual_df)
            manual_prediction_proba = svm_model.predict_proba(manual_df)

            rejected_Percentage=round(manual_prediction_proba[0][0]*100,2)
            Approved_Percentage=round(manual_prediction_proba[0][1]*100,2)

            data_saving=LoanPredictionModel(FullName=fullName, Address=address, Gender=gender, Married=married, Dependence=dependents, Education=education, SelfEmployee=selfEmployed, ApplicantIncome=int(applicantIncome), CoapplicantIncome=int(coapplicantIncome), LoanAmount=int(loanAmount), LoanAmountTerm=int(loanAmountTerm), CreditHistory=int(creditHistory), PropertyArea=propertyArea, RejectedPercentage=rejected_Percentage, ApprovedPercentage=Approved_Percentage, ModelPrediction=manual_prediction[0], LoanStatus=status, )
            data_saving.save()

            return JsonResponse({"message":"ok","Status":status,"Rejected_Percentage":rejected_Percentage,"Approved_Percentage":Approved_Percentage})

        else:
            return JsonResponse({"message":"fields empty"})

        return JsonResponse({"message":"This is post request"})
    else:
        return JsonResponse({"message":"False"})


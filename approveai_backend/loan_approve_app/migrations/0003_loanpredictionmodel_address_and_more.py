# Generated by Django 5.1.3 on 2024-12-02 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_approve_app', '0002_rename_loan_prediction_model_loanpredictionmodel'),
    ]

    operations = [
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='Address',
            field=models.TextField(default='None', max_length=600),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='ApplicantIncome',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='ApprovedPercent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='CoapplicantIncome',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='Credit_History',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='Dependence',
            field=models.TextField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='Education',
            field=models.TextField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='FullName',
            field=models.TextField(default='None', max_length=500),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='Gender',
            field=models.TextField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='LoanAmount',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='LoanStatus',
            field=models.TextField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='Loan_Amount_Term',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='Married',
            field=models.TextField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='ModelPrediction',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='PropertyArea',
            field=models.TextField(default='None', max_length=100),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='RejectedPercent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='loanpredictionmodel',
            name='SelfEmployee',
            field=models.TextField(default='None', max_length=100),
        ),
    ]
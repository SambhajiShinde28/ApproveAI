# Generated by Django 5.1.3 on 2024-12-02 15:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('loan_approve_app', '0003_loanpredictionmodel_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='loanpredictionmodel',
            name='Address',
            field=models.CharField(default='None', max_length=600),
        ),
        migrations.AlterField(
            model_name='loanpredictionmodel',
            name='Dependence',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='loanpredictionmodel',
            name='Education',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='loanpredictionmodel',
            name='FullName',
            field=models.CharField(default='None', max_length=500),
        ),
        migrations.AlterField(
            model_name='loanpredictionmodel',
            name='Gender',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='loanpredictionmodel',
            name='LoanStatus',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='loanpredictionmodel',
            name='Married',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='loanpredictionmodel',
            name='PropertyArea',
            field=models.CharField(default='None', max_length=100),
        ),
        migrations.AlterField(
            model_name='loanpredictionmodel',
            name='SelfEmployee',
            field=models.CharField(default='None', max_length=100),
        ),
    ]

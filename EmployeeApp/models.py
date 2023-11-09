from django.db import models

# Create your models here.

class Contract(models.Model):
    ContractId=models.AutoField(primary_key=True)
    ContractStart=models.DateField()
    ContractEnd= models.DateField()
    ContractPrice=models.CharField(max_length=500)
    ContractDescription=models.CharField(max_length=500)

class Client(models.Model):
     ClientId=models.AutoField(primary_key=True)
     ClientName=models.CharField(max_length=500)
     ClientNIF=models.IntegerField()
     ClientPhone=models.IntegerField()
     ClientEmail=models.CharField(max_length=500)
     ClientAddress=models.CharField(max_length=500)
     ClientPostCode=models.CharField(max_length=500)
  
class Contract_client(models.Model):
     Contract_clientId=models.AutoField(primary_key=True)
     Contract = models.ForeignKey(Contract, on_delete=models.CASCADE)
     Client = models.ForeignKey(Client, on_delete=models.CASCADE)
    


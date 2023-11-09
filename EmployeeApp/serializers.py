from rest_framework import serializers
from EmployeeApp.models import Contract, Client, Contract_client

class ContractSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contract
        fields= ('__all__')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model=Client
        fields=('__all__')

class Contract_clientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Contract_client
        fields = ('__all__')


from django.shortcuts import render

# Create your views here.

from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse
from EmployeeApp.models import Contract,Client, Contract_client
from EmployeeApp.serializers import ContractSerializer, ClientSerializer, Contract_clientSerializer
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.

@csrf_exempt
def ContractApi(request, id=0): 

    if request.method == 'GET':
        contract = Contract.objects.all()
        contract_serializer = ContractSerializer(contract,many=True)
        return JsonResponse(contract_serializer.data,safe=False)

    elif request.method=='POST':
        contract_data = JSONParser().parse(request)
        contract_serializer=ContractSerializer(data=contract_data)
        if contract_serializer.is_valid():
            contract_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method =='PUT':
        contract_data=JSONParser().parse(request)
        contract = Contract.objects.get(ContractId=id)
        contract_serializer = ContractSerializer(contract, data=contract_data)
        if contract_serializer.is_valid():
            contract_serializer.save()
            return JsonResponse("Update Successfully", safe= False)
        return JsonResponse("Failed to Update")
    elif request.method =="DELETE":
        contract=Contract.objects.get(ContractId=id)
        contract.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    

    
@csrf_exempt
def ClientApi(request, id=0):

    if request.method == 'GET':
        client = Client.objects.all()
        client_serializer = ClientSerializer(client,many=True)
        return JsonResponse(client_serializer.data,safe=False)
    elif request.method=='POST':
        client_data = JSONParser().parse(request)
        client_serializer=ClientSerializer(data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)
    elif request.method =='PUT':
        client_data=JSONParser().parse(request)
        client = Client.objects.get(ClientId=id)
        client_serializer = ClientSerializer(client, data=client_data)
        if client_serializer.is_valid():
            client_serializer.save()
            return JsonResponse("Update Successfully", safe= False)
        return JsonResponse("Failed to Update")
    elif request.method =="DELETE":
        client=Client.objects.get(ClientId=id)
        client.delete()
        return JsonResponse("Deleted Successfully", safe=False)
    
@csrf_exempt
def Contract_clientApi(request, id=0):
    if request.method == 'GET':
        contract_client= Contract_client.objects.all()
        contract_clientSerializer = Contract_clientSerializer(contract_client,many=True)
        return JsonResponse(contract_clientSerializer.data,safe=False)
    elif request.method=='POST':
        contract_client_data=JSONParser().parse(request)
    
        contract_clientSerializer=Contract_clientSerializer(data=contract_client_data)
        if contract_clientSerializer.is_valid():
            contract_clientSerializer.save()
            return JsonResponse("Added Successfully", safe=False)
        return JsonResponse("Failed to Add", safe=False)






    



    

from django.shortcuts import render
from .models import Carlist
from django.http import JsonResponse
from .api_file.serializers import CarSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
# from django.http import HttpResponse
# import json

# Create your views here.
# def car_list_view(request):
#     cars = Carlist.objects.all()
#     data = {
#         'cars': list(cars.values()),
#     }
#     # data_json = json.dumps(data)
#     return JsonResponse(data)
#     # return HttpResponse(data_json, content_type='application/json')

@api_view(['GET', 'POST'])
def car_list_view(request):
    if request.method == 'GET':
        cars = Carlist.objects.all()
        serializer = CarSerializer(cars , many=True)
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = CarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

@api_view(['GET', 'PUT'])
def car_detail_view(request, pk):
    
    if request.method == 'GET':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car)
        return Response(serializer.data)
    
    if request.method == 'PUT':
        car = Carlist.objects.get(pk=pk)
        serializer = CarSerializer(car,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
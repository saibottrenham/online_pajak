#from django.shortcuts import render
from django.views import View
from django.http import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
import json
from .models import TaxDataModel

# Create your views here.


@method_decorator(csrf_exempt, name='dispatch')
class ThirdPartyVerification(View):

    def get(self, request):
        items_count = TaxDataModel.objects.count() 
        items = TaxDataModel.objects.all()  

        items_data = []  
        for item in items:
            items_data.append(item)

        data = {
            'items': items_data,
            'count': items_count,
        }
        return JsonResponse(data)
           


@method_decorator(csrf_exempt, name='dispatch')
class TaxDataCommercialRelScoring(View):
    def get(self, request):
        items_count = TaxDataModel.objects.count() 
        items = TaxDataModel.objects.all()  

        items_data = []  
        for item in items:
            items_data.append(item)

        data = {
            'items': items_data,
            'count': items_count,
        }
        return JsonResponse(data)

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
        # Filter Db by company name. If it exist return
        return JsonResponse(
            {"message": "Exists"} if 
            TaxDataModel.objects.filter(company_name=request.GET.get('q'))
            else {"message": "No Entries"}
        )
           


@method_decorator(csrf_exempt, name='dispatch')
class TaxDataCommercialRelScoring(View):
    def get(self, request):
        return JsonResponse({
            "total transactions": TaxDataModel.objects.filter(
                    vendor_id=request.GET.get('vendor_id')
                ).filter(
                    company_id=request.GET.get('company_id')
                ).count()
            })


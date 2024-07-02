from django.shortcuts import render
from django.http import HttpResponse



def customer_service_home(request):
    context={}
    return render(request, "customer_service_template/customer_service_home.html" , context)

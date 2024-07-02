from django.shortcuts import render
from django.http import HttpResponse



def customer_home(request):
    context={}
    return render(request, "customer_template/customer_home.html" , context)

from django.shortcuts import render
from django.http import HttpResponse



def administrator_home(request):
    context={}
    return render(request, "administrator_template/administrator_home.html" , context)

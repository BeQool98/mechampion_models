from django.shortcuts import render
from django.http import HttpResponse



def marketer_home(request):
    context={}
    return render(request, "marketer_template/marketer_home.html" , context)

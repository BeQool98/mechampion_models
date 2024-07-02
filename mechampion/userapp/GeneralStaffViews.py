from django.shortcuts import render
from django.http import HttpResponse



def general_staff_home(request):
    context={}
    return render(request, "general_staff_template/general_staff_home.html", context)

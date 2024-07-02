from django.shortcuts import render
from django.http import HttpResponse



def project_manager_home(request):
    context={}
    return render(request, "project_manager_template/project_manager_home.html" , context)

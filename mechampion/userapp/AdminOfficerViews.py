from django.shortcuts import render
from django.http import HttpResponse


def admin_officer_home(request):
    context={}
    return render(request, "admin_officer_template/admin_officer_home.html" , context)








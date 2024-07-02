from django.shortcuts import render
from django.http import HttpResponse
from . EmailBackEnd import EmailBackEnd

from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.urls import reverse

# Create your views here.
def login_page(request):
    return render(request, "login_user.html")

def login_user(request):
    if request.method!="POST":
         return HttpResponse('<h2>Method not allowed</h2>')
    else:
        user = EmailBackEnd.authenticate(request, username=request.POST.get("email"), password= request.POST.get("password"))
        if user is not  None:
            user.backend = 'userapp.backends.userapp.EmailBackEnd.EmailBackEnd'
            login(request,user)
            if user.user_type == "1":
                return HttpResponseRedirect(reverse('admin_officer_home'))
            
            elif user.user_type == "2":
                return HttpResponseRedirect(reverse("administrator_home"))
            
            elif user.user_type == "3":
                return HttpResponseRedirect(reverse("customer_service_home"))

            elif user.user_type == "4":
                return HttpResponseRedirect(reverse("marketer_home"))
            
            elif user.user_type == "5":
                return HttpResponseRedirect(reverse("project_manager_home"))
            
            elif user.user_type == "6":
                return HttpResponseRedirect(reverse("general_staff_home"))

            else:
                return HttpResponseRedirect(reverse("customer_home")) 
        else: 
            messages.error(request, "invalid Login Details")
            return HttpResponseRedirect("/")
        
    # return render(request, "login_user.html")
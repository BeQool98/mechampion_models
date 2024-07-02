"""
URL configuration for mechampion project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from clientsite import views
from userapp import userviews
from . import settings
from django.conf.urls.static import static

from userapp import AdminOfficerViews, AdministratorViews, CustomerServiceViews, MarketerViews, ProjectManagerViews, GeneralStaffViews, CustomerViews
from . import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('login', userviews.login_page, name='login'),
    path('login_user', userviews.login_user, name='login_user'),
    
    #Admin Officer Views==================================================================
    path('admin_officer/', AdminOfficerViews.admin_officer_home, name='admin_officer_home'),
    
    
    #Admin  Views==================================================================    
    path('administrator/', AdministratorViews.administrator_home, name='administrator_home'),
    
    #Customer Service Views==================================================================    
    path('customer_service/', CustomerServiceViews.customer_service_home, name='customer_service_home'),
    
    #Marketer Views==================================================================
    path('marketer/', MarketerViews.marketer_home, name='marketer_home'),
    
    #Project Manager Views==================================================================
    path('project_manager/', ProjectManagerViews.project_manager_home, name='project_manager_home'),
    
    #Staff Views==================================================================
    path('staff/', GeneralStaffViews.general_staff_home, name='general_staff_home'),
    
    #Customer Views==================================================================
    path('customer/', CustomerViews.customer_home, name='customer_home'),
    
   
    
]

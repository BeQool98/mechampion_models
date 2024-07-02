from django.utils.deprecation import MiddlewareMixin
from django.urls import reverse
from django.http import HttpResponseRedirect

class LoginCheckMiddleWare(MiddlewareMixin):
    def process_view(self, request, view_func, view_args, view_kwargs):
        modulename = view_func.__module__
        user = request.user
        
        if user.is_authenticated:
            if user.user_type == "1":
                if modulename == "userapp.AdminOfficerViews":
                    pass
                elif modulename == "userapp.userviews" or modulename == "django.views.static":
                    pass
                else: 
                    return HttpResponseRedirect(reverse("admin_officer_home"))
                
                
            elif user.user_type == "2":
                if modulename == "userapp.AdministratorViews":
                    pass
                elif modulename == "userapp.userviews" or modulename == "django.views.static":
                    pass
                else: 
                    return HttpResponseRedirect(reverse("administrator_home"))
                
            elif user.user_type == "3":
                if modulename == "userapp.CustomerServiceViews":
                    pass
                elif modulename == "userapp.userviews" or modulename == "django.views.static":
                    pass
                else: 
                    return HttpResponseRedirect(reverse("customer_service_home"))
                
            elif user.user_type == "4":
                if modulename == "userapp.MarketerViews":
                    pass
                elif modulename == "userapp.userviews" or modulename == "django.views.static":
                    pass
                else: 
                    return HttpResponseRedirect(reverse("marketer_home"))
                
            elif user.user_type == "5":
                if modulename == "userapp.ProjectManagerViews":
                    pass
                elif modulename == "userapp.userviews" or modulename == "django.views.static":
                    pass
                else: 
                    return HttpResponseRedirect(reverse("project_manager_home"))
                
                
            elif user.user_type == "6":
                if modulename == "userapp.GeneralStaffViews":
                    pass
                elif modulename == "userapp.userviews" or modulename == "django.views.static":
                    pass
                else: 
                    return HttpResponseRedirect(reverse("general_staff_home"))

            elif user.user_type == "7":
                if modulename == "userapp.CustomerViews":
                    pass
                elif modulename == "userapp.userviews" or modulename == "django.views.static":
                    pass
                else: 
                    return HttpResponseRedirect(reverse("customer_home"))


            else:
                return HttpResponseRedirect(reverse("show_login"))    
            
                
                
                
                    
            
        else:
            if request.path == reverse("show_login") or request.path == reverse("do_login") or modulename=="django.contrib.auth.views":
                pass
            else:
                return HttpResponseRedirect(reverse("show_login"))
    
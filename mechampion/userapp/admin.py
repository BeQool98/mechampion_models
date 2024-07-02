from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from userapp.models import CustomUser
from .models import *

# Register your models here.
class UserModel(UserAdmin):
    pass

admin.site.register(CustomUser, UserModel)
admin.site.register(AdminOfficer)
admin.site.register(Administrator)
admin.site.register(CustomerService)
admin.site.register(Marketer)
admin.site.register(ProjectManager)
admin.site.register(GeneralStaff)
admin.site.register(Customer)




from django.contrib.auth.models import AbstractUser
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class CustomUser(AbstractUser):
    user_type_data = ((1, "AdminOfficer"), (2, "Administrator"),(3, "CustomerService"),(4, "Marketer"), (5, "ProjectManager"), (6, "GeneralStaff"), (7, "Customer"))
    user_type = models.CharField(default = 1, choices = user_type_data, max_length = 10)
    try:
        def __str__(self):
            return self.username
    except NoneType:
        pass
    
class AdminOfficer(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser,  related_name='adminofficer', on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
    
class Administrator(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser,  related_name='administrator', on_delete = models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now_add=True)
    objects = models.Manager()
    
class CustomerService(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser,  related_name='customerservice',on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()
    
class Marketer(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser,  related_name='marketer',on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()
    
class ProjectManager(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser,  related_name='projectmanager', on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()
    
class GeneralStaff(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser,  related_name='generalstaff', on_delete = models.CASCADE)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()
    
class Customer(models.Model):
    id = models.AutoField(primary_key = True)
    admin = models.OneToOneField(CustomUser,  related_name='customer', on_delete = models.CASCADE)
    address = models.TextField()
    gender = models.CharField(max_length = 10)
    profile_pic = models.FileField()
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add =True)
    updated_at = models.DateTimeField(auto_now_add = True)
    objects = models.Manager()
    
    
    
@receiver(post_save, sender = CustomUser)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.user_type==1:
            AdminOfficer.objects.create(admin  = instance)
        
        if instance.user_type==2:
            Administrator.objects.create (admin = instance)
            
        if instance.user_type==3:
            CustomerService.objects.create(admin=instance)
        if instance.user_type==4:
            Marketer.objects.create(admin=instance)
            
        if instance.user_type==5:
            ProjectManager.objects.create(admin=instance)
            
        if instance.user_type==6:
            GeneralStaff.objects.create(admin=instance)
            
        if instance.user_type==7:
            Customer.objects.create(admin=instance)


@receiver(post_save, sender = CustomUser)        
def save_user_profile(sender, instance, **kwargs):
    if instance.user_type==1:
        instance.adminofficer.save()
        
    if instance.user_type==2:
        instance.administrator.save()
        
    if instance.user_type==3:
        instance.customerservice.save()
        
    if instance.user_type==4:
        instance.marketer.save()
        
    if instance.user_type==5:
        instance.projectmanager.save()
        
    if instance.user_type==6:
        instance.generalstaff.save()
        
    if instance.user_type==7:
        instance.customer.save()
        
        
            

        

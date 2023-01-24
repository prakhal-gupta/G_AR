from email.policy import default
from django.db import models
from .models import *


class G_Block(models.Model):
    Room_No                 = models.CharField(max_length=10,primary_key=True)
    Floor                   = models.CharField(max_length=20,null=True)
    Room_Type               = models.CharField(max_length=50,null=True)
    Fac_Seating_capacity    = models.IntegerField(null=True)
    Fac_Presently_occupied  = models.IntegerField(null=True)
    Current_Use             = models.CharField(max_length=50,null=True)


class G_Faculty_Detail(models.Model):
    Fac_Room_No             = models.ForeignKey(G_Block,on_delete=models.CASCADE)
    Faculty_Name            = models.TextField(max_length=100, null=True)
    Faculty_Dept            = models.CharField(max_length=50,null=True)
    # Fac_Profile_pic         = models.ImageField(upload_to='Profile_pic/', default='static/profile-default.png')
    
class Con_Student_Detail(models.Model):
    First_Name               = models.CharField(max_length=50, null=True)
    Last_Name                = models.CharField(max_length=50,null=True) 
    Email                    = models.EmailField(max_length= 80,null=True)    
    Message                  = models.TextField(max_length=100, null=True)  
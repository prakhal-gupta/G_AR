import json
from django.http  import JsonResponse
from .models import *
import re
# from django.contrib.auth import authenticate, login, logout
# from django.contrib.auth.models import User
# import re,os,random,string
# from django.core.mail import send_mail
# from datetime import date


def Room_Registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)

        if (G_Block.objects.filter(Room_No = data['Room_No'])):
            mes = {'error': 'Room Already Used!!'}
            return JsonResponse(mes,status=403,safe=False)
        else:
            new_room=G_Block(**data)
            new_room.save()
            mes = {'message': 'Room Details Saved!!'}
            return JsonResponse(mes,status=200,safe=False)


def Room_Detail(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Room = data['Room_No']
        if (G_Block.objects.filter(Room_No = Room).exists()):
               Room_d  =G_Block.objects.get(Room_No = Room)
               mes = {      
                    'Room_No'    :Room_d.Room_No ,
                    'Floor'      :Room_d.Floor,
                    'Room_Type'  :Room_d.Room_Type,
                    'Current_Use'  :Room_d.Current_Use  }
               return JsonResponse(mes,status=200,safe=False)
        else:   
            mes = {'error':'Room not exists!'}
            return JsonResponse(mes,status=403,safe=False)


def Room_delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Room_No_d     = data['Room_No']
        if (G_Block.objects.filter(Room_No=Room_No_d).exists()):
            Room  = G_Block.objects.get(Room_No=Room_No_d)
            Room.delete()
            mes = { 'message' : "Room Data Deleted!"} 
            return JsonResponse(mes,status=200,safe=False)
        else:
            mes = { "error"   :"No Such Room Exists!"}
            return JsonResponse(mes,status=403,safe=False)



def Faculty_Registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        if (G_Faculty_Detail.objects.filter(Faculty_Name = data['Faculty_Name'])):
            mes = {'error': 'Faculty Room Already Alloted!!'}
            return JsonResponse(mes,status=403,safe=False)
        
        else:
            Room_c = G_Block.objects.get(Room_No=data['Room_No'])
            Capacity_c  =Room_c.Fac_Seating_capacity
            occupied_c =Room_c.Fac_Presently_occupied
            if(occupied_c==Capacity_c):
                mes = {'error': 'Faculty Room Full!!'}
                return JsonResponse(mes,status=403,safe=False)
            else:
                occupied_n = occupied_c + 1
                Room_c.Fac_Presently_occupied = occupied_n
                Room_c.save(update_fields=['Fac_Presently_occupied'])
                data['Fac_Room_No']= Room_c
                del[data['Room_No']]
                new_Faculty=G_Faculty_Detail(**data)
                new_Faculty.save()
                mes = {'message': 'Faculty Details Saved!!'}
                return JsonResponse(mes,status=200,safe=False)

    
def Faculty_detail(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Room = data['Room_No']
        if (G_Block.objects.filter(Room_No = Room).exists()):
            Room_d  =G_Block.objects.get(Room_No = Room)

            if (G_Faculty_Detail.objects.filter(Fac_Room_No = Room_d).exists()):
                Faculty_d       = G_Faculty_Detail.objects.filter(Fac_Room_No = Room_d)
                Faculty_det     = list(Faculty_d.values('Fac_Room_No','Faculty_Name','Faculty_Dept'))
                mes = { 'Faculty_detail' : Faculty_det}
                return JsonResponse(mes,status=200,safe=False)
            else:
                mes = {  "error"   :"This is not Faculty Room!"}
                return JsonResponse(mes,status=403,safe=False)
        else:
                mes = {  "error"   :"Room Not Exists!"}
                return JsonResponse(mes,status=403,safe=False) 


def Faculty_delete(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Faculty_d     = data['Faculty_Name']
        if (G_Faculty_Detail.objects.filter(Faculty_Name=Faculty_d).exists()):
            Faculty = G_Faculty_Detail.objects.get(Faculty_Name=Faculty_d)
            Faculty.delete()
            mes = { 'message' : "Faculty Room Unallocated!"} 
            return JsonResponse(mes,status=200,safe=False)
        else:
            mes = { "error"   :"No Such Faculty Exists!"}
            return JsonResponse(mes,status=403,safe=False)



def G_Faculty_All_Detail(request):
    if request.method == 'GET':
        Faculty_d  =list(G_Faculty_Detail.objects.all().values('id','Faculty_Name'))
        # Faculty_det     = list(Faculty_d.values('id','Faculty_Name'))
        # mes = {'Faculty' : Faculty_det}
        return JsonResponse(Faculty_d,status=200,safe=False)



def Faculty_Room_Detail(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        Id_d = data['key']
        print(data)
        if (G_Faculty_Detail.objects.filter(id = Id_d).exists()):
            Room_d  =G_Faculty_Detail.objects.get(id = Id_d)
            mes = {      
                'Room_No'    :Room_d.Fac_Room_No.Room_No ,
                'Fac_Name'   :Room_d.Faculty_Name,
                'Fac_Dept'   :Room_d.Faculty_Dept  }
            return JsonResponse(mes,status=200,safe=False)
        else:   
            mes = {'error':'Faculty Not in G-Block!'}
            return JsonResponse(mes,status=403,safe=False)



def Con_Student_Registration(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        email_condition  = "[a-zA-Z0-9\-\_\.]+@[a-zA-Z0-9]{2,}\.[a-zA-Z0-9]{2,3}$"
        match   = re.search(email_condition,data['Email'])
        if (not match):
            mes = { 'error': 'Invalid Email !'}
            return JsonResponse(mes,status=403,safe=False)

        if (Con_Student_Detail.objects.filter(Email = data['Email'])):
            mes = {'error': 'Email Already Exists!!'}
            return JsonResponse(mes,status=403,safe=False)
        else:
            new_room=Con_Student_Detail(**data)
            new_room.save()
            mes = {'message': 'Student Details Saved!!'}
            return JsonResponse(mes,status=200,safe=False)    






























       
            

        




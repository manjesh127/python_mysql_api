from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
import json
from .models import employee

def hello(request):
    text = """<h1>welcome to my app !</h1>"""
    return HttpResponse(text)

def insertApi(request):
    if request.method =="POST":
        data=json.loads(request.body)
        empl_id=data["id"]
        first_name=data["fname"]
        last_name = data["lname"]
        job_title=data["title"]
        salary = data["salary"]
        office_id =data["offid"]
        employee_info = employee(employee_id=empl_id,first_name=first_name,last_name=last_name,job_title=job_title,salary=salary,office_id=office_id)
        employee_info.save()
        return JsonResponse({'success':True,'message':'save detail success'})
    else:
        return JsonResponse({'success':False,'message':'save detail failed'})
    

def getApi(request):
    if request.method =="GET":
        fetch = employee.objects.all()
        tmpJson = serializers.serialize("json",fetch)
        data = json.loads(tmpJson)
        for d in data:
            del d['pk']
            del d['model']
        return JsonResponse({'success':True,'message':'Fetch success','data':data})
    
    else:
        return JsonResponse({'success':False,'message':'Invalid request'})
        
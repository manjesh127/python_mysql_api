from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.http import JsonResponse
from django.core import serializers
from django.conf import settings
import json
import ujson
import requests
from .models import employee
import jwt
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated


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
        
        
def emplyLogin(request):
    if request.method =="POST":
        data = json.loads(request.body)
        first_name = data["fname"]
        last_name = data["lname"]   
        getData = employee.objects.filter(first_name=first_name,last_name=last_name)
        tmpJson = serializers.serialize("json",getData)
        resp_json = json.loads(tmpJson)
        for d in resp_json:
            del d['pk']
            del d['model']
            
        if len(resp_json) ==0:
            return JsonResponse({'success':False,'message':'Invalid credentials'})
        else:
            encoded_jwt = jwt.encode({'first_name':resp_json[0]["fields"]["first_name"],'last_name':resp_json[0]["fields"]["last_name"] }, settings.SECRET_KEY, algorithm='HS256')

            return JsonResponse({'success':True,'message':'success','token':ujson.loads(ujson.dumps(encoded_jwt))})

    else:
        return JsonResponse({'success':False,'message':'Invalid request'})


def verifyLogin(request):
    # print(request.META['HTTP_AUTHORIZATION'].split()[1])
    if request.method=="POST":
        decoded = jwt.decode(request.META['HTTP_AUTHORIZATION'].split()[1],settings.SECRET_KEY , algorithms='HS256')
        return JsonResponse({'success':True,'message':'valid jwt','name':decoded["first_name"]})

    else:
        return JsonResponse({'success':False,'message':'Invalid request'})
   
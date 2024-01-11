from django.shortcuts import render
from django.http import HttpResponse
from app.models import *

# Create your views here.

def school(request):
    if request.method=='POST':
        sn=request.POST['sn']
        sl=request.POST['sl']
        sp=request.POST['sp']
        SO=School.objects.get_or_create(sname=sn,sloc=sl,sprinci=sp)[0]
        SO.save()
        return HttpResponse('School Data has been Inserted')
    return render(request,'school.html')

def student(request):
    if request.method=='POST':
        std=request.POST.get('std')
        sn=input()
        SNO=School.objects.get(sname=sn)
        stn=request.POST.get('stn')
        stp=request.POST.get('stp')
        STO=Student.objects.get_or_create(sid=std,sname=SNO,stname=stn,stphone=stp)[0]
        STO.save()
        return HttpResponse('Student Data has been Inserted')
    return render(request,'student.html')
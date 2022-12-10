from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
import csv
from django.http import HttpResponse
from home.theft import abc,sus
import pandas as pd
# Create your views here.
d = pd.read_csv('home/data.csv')


def index(request):
    if request.user.is_anonymous:
        return redirect("/login")
    return render(request,"index.html")
def user_info(request):
    if request.user.is_anonymous:
        return redirect('/login')
    alldata=[]
    for i in range(d.shape[0]):
        temp = d.iloc[i]
        alldata.append(dict(temp))
    abc = {'DATA': alldata}
    

    return render(request,'userinfo.html',abc)
def actual_bill(request):
    if request.user.is_anonymous:
        return redirect('/login')
    alldata=[]
    for i in range(d.shape[0]):
        temp = d.iloc[i]
        alldata.append(dict(temp))
    abc = {'DATA': alldata}
    
    return render(request,'actualbill.html',abc)
def suspect(request):
    if request.user.is_anonymous:
        return redirect('/login')
    alldata=[]
    for i in range(d.shape[0]):
        temp = d.iloc[i]
        alldata.append(dict(temp))
    abc = {'DATA': alldata}
    return render(request,'suspect.html',abc)
def register(request):
    if request.user.is_anonymous:
        return redirect('/login')
    alldata=[]
    for i in range(d.shape[0]):
        temp = d.iloc[i]
        alldata.append(dict(temp))
    abc = {'DATA': alldata}
           
        
    return render(request,"BILLPREDICTION.html",abc)
def loginuser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username= username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/login/home')
            
        else:
            return render(request,"login.html")
            

    return render(request,"login.html")
def logout_user(request):
    logout(request)
    return redirect('/login')
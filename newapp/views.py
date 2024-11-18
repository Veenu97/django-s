from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from newapp.form import StuForm
import datetime
def content(request):
    return HttpResponse("<h1><center>WELCOME TO THE WEBSITE<center></h1>")

def content1(request):
    a=15
    b=25
    return HttpResponse(a+b)
def content2(request):
    a=35
    b=25
    return HttpResponse(a-b)
def content3(request):
    a=12
    b=12
    return HttpResponse(a*b)
def content4(request):
    a=526
    b=2
    return HttpResponse(a/b)
def content5(request):
    l=12
    b=9
    h=10
    return HttpResponse(l*b*h)
def content6(request):
    side=17
    return HttpResponse(side*side*side)
def content7(request):
    l=13
    b=15
    return HttpResponse(2*(l+b))
def content8(request):
    side=14
    return HttpResponse(4*side)
def content9(request):
    l=14
    b=7
    return HttpResponse(l*b)
def content10(request):
    side=8
    return HttpResponse(side*side)


def new(request):
    template=loader.get_template('index.html')
    return HttpResponse(template.render())

def sume(request):
    template=loader.get_template('resume.html')
    return HttpResponse(template.render())

def dt(request):
    now= datetime.datetime.now()
    html="<html><body><h3>Now time is %s.</h3></body><html>"%now
    return HttpResponse(html)  #rendering the template in HttpResponse
 
def h1(request):
    template=loader.get_template('home.html')
    return HttpResponse(template.render())
 
def a1(request):
    template=loader.get_template('about.html')
    return HttpResponse(template.render())
def form(request):
    stu = StuForm()
    return render(request,"form.html",{'form':stu})


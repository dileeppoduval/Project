from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def myfunction(request):
    return HttpResponse("this is my first program")
def myfunction2(request):
    return HttpResponse("this s second")
def myfunction3(request):
    return HttpResponse("this is my third home page")
def myfunctiontest(request):
    return render(request,'index.html')
def mytable(request):
    return render(request,'table.html')
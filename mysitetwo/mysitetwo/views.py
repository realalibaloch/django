from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    return render(request,'index.html')
def aboutus(request):
    return HttpResponse('Welcome Ali on home page')
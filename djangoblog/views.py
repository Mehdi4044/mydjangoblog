from django.shortcuts import render
from django.shortcuts import HttpResponse


def about (request):
    # return HttpResponse(' Hello My world')
    return render(request,'about.html')



def home(request):
    # return HttpResponse('it is my Home')
    return render(request,'Home.html')

from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def rcb(request):
    return render (request,'rcb.html')

def virat(request):
    return HttpResponse('<h1> virat is woderful player</h1>')
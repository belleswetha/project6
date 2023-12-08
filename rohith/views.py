from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def mi(request):
    return render(request,'mi.html')

def rohith(request):
    return HttpResponse ('<h1>rohith sharma king of mumbai team</h1>')
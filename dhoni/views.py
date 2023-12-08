from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.
def csk(request):
    return render(request,'csk.html')
 
def dhoni(request):
    return HttpResponse('<h1>dhoni is king of csk</h1>')
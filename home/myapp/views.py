from django.shortcuts import render
from django.http import HttpResponse



# Create your views here.


def home(request):
    return render(request,'index.html')


def submit(request):
    return HttpResponse("<b><h1>You submitted data </b></h1>")
                        

#def dome(request):
    #return HttpResponse("<h2> Hello Guys!!</h2>")


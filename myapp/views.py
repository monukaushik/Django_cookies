from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
   
   return render(request,'index.html')

def set_cookie(request):
   response=render(request,'set_cookie.html')
   response.set_cookie('name','monu kaushik',max_age=3600 , expires=None)     # set the cookies in client browser in dict ( key and value) form
   return response
   # return render(request,'set_cookie.html')


def get_cookie(request):
   get_name=request.COOKIES['name']  
   # get_name=request.COOKIES.items()                                         # get the key and value of cookies
   return render(request,'get_cookie.html',{'get_name':get_name})

def updateCookie(request):
    response = render(request,"update.html")
    response.set_cookie("name","Mohan")
    return response


def del_cookie(request):
   
   response= render(request,'del_cookie.html')
   response.delete_cookie('name')                                            # delete the cookies from the browser
   # request.COOKIES.pop('name') 
   return response


   # return render(request,'del_cookie.html')
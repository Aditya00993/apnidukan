from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseBadRequest
from .models import Ram,Con
from math import ceil
from datetime import datetime 


# Create your views here.
def index(request):
    return render(request,'home.html')

def login(request):
   
  
   # paramas = {'nslide':nslide, 'range':range, 'product':products}
    allproducts =[]
    catprods = Ram.objects.values('category','id')
    cats = {item['category'] for item in catprods}
    for cat in cats:
        pro = Ram.objects.filter(category = cat)
        n=len(pro)
        nslide = n//4 + ceil((n/4)-(n//4))
        allproducts.append([pro,range(1,nslide),nslide])
       
    params ={'allproducts':allproducts}
    return render(request,'shop.html',params)


def error(request):
    return render(request,'home.html')

def Contact(request):
    if request.method == 'POST':
     name = request.POST.get('name')
     email = request.POST.get('email')
     phone = request.POST.get('phone')
     message = request.POST.get('message')
     con = Con(name=name,email=email,phone=phone,message=message) 
     con.save()
    return render(request,'contact.html')

def about(request):
    return render(request,'abaut.html')

def tracker(request):
    return render(request,'tracker.html')

def checkout(request):
    return render(request,'checkout.html')

def product(request,myid):
    product = Ram.objects.filter(id=myid)
    return render(request,'product.html',{'product':product[0]})

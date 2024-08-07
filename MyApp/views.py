from django.shortcuts import render, HttpResponse
from . models import Asset

# Create your views here.
def homepage(request):

    items = Asset.objects.all()
    
    return render(request,'index/index.html',{'items':items,})
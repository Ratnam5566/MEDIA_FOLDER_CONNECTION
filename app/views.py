from django.shortcuts import render
from django.http import HttpResponse
from app.forms import *

# Create your views here.
def reg(request):
    ufo=UserForm()
    pfo=ProfileForm()
    d={'ufo':ufo,'pfo':pfo}
    if request.method=='POST' and request.FILES:
        ufd=UserForm(request.POST)
        pfd=ProfileForm(request.POST,request.FILES)
        if ufd.is_valid() and pfd.is_valid():
            USUFO=ufd.save(commit=False)
            subpw=ufd.cleaned_data['password']
            USUFO.set_password(subpw)
            USUFO.save()
            USPFO=pfd.save(commit=False)
            USPFO.username=USUFO
            USPFO.save()
            return HttpResponse('Registration Is successfully Done')
    return render (request,'registration.html',d)

def display(request):
    obj=Profile.objects.all()
    obj1=User.objects.all()
    d={'obj':obj,'obj1':obj1}
    return render (request,'dispaly.html',d)

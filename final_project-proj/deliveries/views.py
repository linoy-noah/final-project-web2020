from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, authenticate
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.contrib.auth import logout,login
from .forms import deliveryForm
from .models import deliveries
from django.contrib.auth.decorators import login_required


# Create your views here.
def needlogin(request):
    return render(request,'index.html',{"errMsg":"Need to login first."})

def loginuser(request):
    if request.method == 'GET':
        return render(request,'login.html', {'form':AuthenticationForm()})
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        if user is None:
            return render(request,'login.html', {'form':AuthenticationForm(),'errMsg':'User does not exists'})
        else:
            login(request,user)
            return redirect('homepage')

@login_required
def myDeliveries(request):
    mydels = deliveries.objects.filter(sender = request.user).order_by('-status')
    return render(request,'mydeliveries.html',{'deliveries':mydels})

@login_required
def showDelivery(request,delivery_pk):
    delivery = get_object_or_404(deliveries,pk=delivery_pk,sender=request.user)
    return render(request, 'progress.html',{'d':delivery})

@login_required
def makeDelivery(request):
    myDel= deliveries.objects.exclude(sender=request.user).filter(deliveryman = request.user).order_by('-status')
    allnewdels= deliveries.objects.exclude(sender=request.user).filter(status = 0)
    return render(request,'makeDelivery.html',{'deliveries':myDel , 'newdeliveries':allnewdels})

@login_required
def updatestat(request,delivery_pk):
    delivery = get_object_or_404(deliveries,pk=delivery_pk)
    if request.method == "POST":
        if delivery.status < 3:
            delivery.deliveryman = request.user
            delivery.status = delivery.status + 1
            delivery.save()
    return redirect('makeDelivery')

@login_required
def deleteDelivery(request,delivery_pk):
    delivery = get_object_or_404(deliveries,pk=delivery_pk,sender=request.user)
    if request.method == 'POST':
        delivery.delete()
        return redirect('myDeliveries')

@login_required
def order(request):
    if request.method == 'GET':
        return render(request,'order.html',{'form':deliveryForm()})
    else:
        try:
            form = deliveryForm(request.POST)
            newDelivery = form.save(commit=False)
            newDelivery.sender = request.user
            newDelivery.save()
            return redirect('myDeliveries')
        except ValueError:
            return render(request,'order.html',{'form':deliveryForm(),'errMsg':"Data mismatch."})

@login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
    return redirect('homepage')

def homepage(request):
    return render(request,'index.html')


def registerform(request):
    if request.method == 'GET':
        return render(request,'register.html',{'form':UserCreationForm()})
    else:
        if request.POST['password1']==request.POST['password2']:
            try:
                user= User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                user.save()
                login(request,user)
                return redirect('homepage')
            except IntegrityError:
                return render(request,'register.html',{'form':UserCreationForm(),'errMsg':'User name exist. Choose a different one.'})
        else:
            return render(request,'register.html',{'form':UserCreationForm(),'errMsg':'Password did not match.'})

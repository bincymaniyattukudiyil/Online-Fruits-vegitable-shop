from django.contrib import messages, auth
from django.shortcuts import render, redirect
from shop.models import *
from django.contrib.auth.models import User


# Create your views here.
from django.http import HttpResponse



def register(request):
    if request.method=='POST':
        first_name=request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        Contact=request.POST['Contact']
        if Profile.objects.filter(username=username).exists():

            messages.info(request,"username exist")
            return redirect('register')
        else:
            shopuser=Profile(first_name=first_name,last_name=last_name,email=email,password=password,username=username,Contact=Contact)
            shopuser.save();
            user = User.objects.create_user(password=password,
                                            username=username)
            user.save();
        return render(request, 'index.html')

    else:
        return render(request,'Register.html')

def login(request):
    print("here")
    print(request.method )
    if request.method =='POST':
        print("here1")
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return render(request, 'index.html',{'username':username})
        else:

            return redirect('home')

    else:
        # messages.info(request,"user doesnot exist")
     return render(request, 'Login.html')
def logout(request):
   # return HttpResponse("hi")
    auth.logout(request)
    return render(request, 'index.html')





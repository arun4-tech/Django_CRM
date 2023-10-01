from django.shortcuts import render, redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

def home(request):
  #Check to see if loggin in
  if request.method == 'POST':
     uname = request.POST['username']
     passwd = request.POST['password']
     #Authenticate
     user = authenticate(request, username=uname, password=passwd)
     if user is not None:
      login(request,user)
      messages.success(request,"You have been Logged In")
      return redirect('home')
     else:
      messages.success(request,"There was a error Logging In, Please Try Again...")
      return redirect('home')
  else:
     return render(request, 'home.html',{})


def logout_user(request):
    logout(request)
    messages.success(request,"You have been Logged Out...")
    return redirect('home')

def register_user(request):
  return render(request, 'register.html',{})
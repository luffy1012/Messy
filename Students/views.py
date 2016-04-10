from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth import authenticate,login

def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/profile/')
    if request.method=="POST":
        print "post"
        form = LoginForm(request.POST)
        if form.is_valid():
            print "form is valid"
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            print username,password
            student = authenticate(username=username,password=password)
            if student is not None:
                print "Logging In!"
                login(request,student)
                return HttpResponseRedirect('/profile/')
    form = LoginForm()
    context = {'form':form}
    return render(request,"Students/login.html",context)

def Profile(request):
    if request.user.is_authenticated():
        return HttpResponse("You are logged in!!")

from django.shortcuts import render
from .forms import LoginForm
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
from .models import Student
def LoginRequest(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/home/')
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
                return HttpResponseRedirect('/home/')
    form = LoginForm()
    context = {'form':form}
    return render(request,"Students/login.html",context)

def Home(request):
    if request.user.is_authenticated():
        usr = Student.objects.get(user=request.user)
        return render(request,"Students/home.html",{'user':usr})

def Account(request):
    if request.user.is_authenticated():
        usr = Student.objects.get(user=request.user)
        return render(request,"Students/account.html",{'user':usr})

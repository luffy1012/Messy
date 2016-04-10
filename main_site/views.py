from django.shortcuts import render
from django.http import HttpResponse


def login(request):
    if request.method == "POST":
        usr = request.POST.get('username')
        pwd = request.POST.get('pwd')
        print usr
        print pwd
       # try:
            #student = Student.objects.get(username=usr)
       # except:
            #return render(request,'main_site/login.html')
       # else:
           # if student.password == pwd:
              #  return HttpResponse("Name - {0}\nEntry-No - {1}\n".format(student.name,student.entry_num))
    return render(request,"main_site/login.html")
def user(request):
    return HttpResponse("hello user!")
# Create your views here.

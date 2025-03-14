# Program to implement Django authentication:
from django.shortcuts import render,redirect,HttpResponse
from django.views import View
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User

# Create your views here.
class MyView(View):
    def get(self,request):
        return render(request,"myapp/index.html",{})

    def post(self,request):
        uname = request.POST.get("username")
        passwd = request.POST.get("password")
        user = authenticate(username = uname,password = passwd)
        if user is not None:
            login(request,user)
            return redirect("myapp:login")
        else:
            return HttpResponse(f"Please signup <b>{uname}</b>")

# View for login:
class LoginView(View):
    def get(self,request):
        return render(request,"myapp/login.html",{})

# Registration:
def register(request):
    if request.method == "POST":
        uname = request.POST.get("username")
        passwd = request.POST.get("password")
        user = User.objects.create_user(username = uname,password = passwd)
        # Adding login functionality:
        login(request,user)
        return redirect("myapp:login")

# Log out functionality:
def log_out(request):
    logout(request)
    return redirect("myapp:index")
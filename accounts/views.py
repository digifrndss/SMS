from django.shortcuts import render,redirect,HttpResponse
from django.contrib import auth
from .models import *
from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control



def login(request):
    if request.method =='POST': 
        user= auth.authenticate(username=request.POST['username'],password=request.POST['password'])
        if user is not None:
            auth.login(request,user)

            return redirect('accounts:dashboard')
        else:
            error ="User Name or Password is Incorrect!!!"
            return render(request, 'login.html')  
    else:
        return render(request, 'login.html')




@login_required
@cache_control(no_cache=True, must_revalidate=True, no_store=True)
def index(request):
    if request.user.is_superuser:
        return render(request, 'dashboard.html')
    else:
        user=User_reg.objects.filter(user_id=request.user.id)
        print(user)
    return  render(request, 'dashboard.html')




def logout(request):
    auth.logout(request)
    return redirect('accounts:login')

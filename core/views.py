from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

from django.contrib.auth import authenticate, login



# Create your views here.

def index(request):
    return redirect(core_home)

@login_required(login_url='/core/login')
def core_home(request):
    return render(request, 'core/index.html', {})

def core_sign_up(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
            )
        if user is not None:
            login(request, user)

        return redirect(core_home)


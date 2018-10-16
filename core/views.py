from django.http import HttpResponse
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
        
        # Проверить, что браузер принимает cookie:
        if request.session.test_cookie_worked():

            # Браузер принимает, удаляем тестовый cookie.
            request.session.delete_test_cookie()

            user = authenticate(
                username=request.POST['username'],
                password=request.POST['password']
                )
            if user is not None:
                login(request, user)
        else:
            return HttpResponse("Please enable cookies and try again.")

        # Если мы не отсылали форму, отправляем тестовое cookie
        # вместе с формой аутентификации.
        request.session.set_test_cookie()
        return redirect(core_home)


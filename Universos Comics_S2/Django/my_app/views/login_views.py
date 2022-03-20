from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render


def login_system(request):
    if request.method == 'POST':
        _user = request.POST['user']
        _password = request.POST['paswd']

        user  = authenticate ( request , username = _user , password = _password)
        if user:
            login(request,user)
            return redirect('characters')
        else:
            return render(request,'characters\\login.html',{'Error':'Usuario o contraseña incorrectos'})

    return render(request,'characters\\login.html',{'Usuario': login_system})

@login_required
def logout_system(request):
    logout(request)
    return render(request,'characters\\index.html')
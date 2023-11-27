from django.shortcuts import render

# Create your views here.
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect


# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

def register(request):
    if request.method == 'POST':
        uname = request.POST['user_name']
        password = request.POST['password']
        conpassword = request.POST['conpassword']

        if password == conpassword:
            if User.objects.filter(username=uname).exists():
                messages.error(request, 'Username already taken')
            else:
                user = User.objects.create_user(username=uname, password=password)
                user.save()
                messages.success(request, 'Registration successful. You can now log in.')
                return redirect('/credentials/login')
        else:
            messages.error(request, 'Password mismatched')

    # If there's an error or the request method is not POST, return to the registration page
    return render(request, 'register.html')

def login(request):
        if request.method == 'POST':
                uname = request.POST['user_name']
                password = request.POST['password']

                user = auth.authenticate(username=uname, password=password)

                if user is not None:
                        auth.login(request, user)
                        return redirect('/user')

                else:
                        messages.info(request, 'Invalid Credentials')
                        return redirect('login')
        return render(request, 'login.html')

def logout(request):
                auth.logout(request)
                return redirect('/')

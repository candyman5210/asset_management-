from django.shortcuts import redirect, render
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def registration(request):
    if request.method == 'POST' :
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        first_name = request.POST['first_name']
        confirmPassword = request.POST['confirmPassword']
        
        if password == confirmPassword:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'username taken')
                
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'email already registered')
                
            else:
                user = User.objects.create_user(first_name=first_name, email=email, password=password, username = username)
                user.save();
                print('user created scecufukky')
                return redirect('registration:login')
        else:
            print('password mismatch')
    else : 
        pass
    return render(request, 'form/form.html')


def login(request):
    return render(request, 'form/login_form.html')
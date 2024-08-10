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
                return redirect('registration:registration')
                
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'email already registered')
                
            else:
                user = User.objects.create_user(first_name=first_name, email=email, password=password, username = username)
                user.save();
                messages.info(request,'user crested sucesfully')
                return redirect('registration:login')
        else:
            print('password mismatch')
            messages.info(request, 'Password mismatch')
            return redirect('registration:registration')
    else : 
        return render(request, 'form/form.html')
    
    
    return render(request, 'form/form.html')


def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = request.POST['username']
        
        user = auth.authenticate(email=email,password=password,username =username)
        
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'welcome')
            return redirect('MyApp:homepage')
        else:
            messages.info(request, 'invalid credentials !!!')
            return redirect('registration:login')
        
    else:
        return render (request, 'form/login_form.html')
    

def sign_out(request):
    auth.logout(request)
    return redirect('MyApp:homepage')
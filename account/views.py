from django.shortcuts import render , redirect
from django.contrib import messages
from django.contrib.auth.models import User , auth

# Create your views here.

def user_registration(request):
   if request.method == 'POST':
       first_name = request.POST.get('first_name')
       last_name = request.POST.get('last_name')
       user_name = request.POST.get('user_name')
       email = request.POST.get('email')
       mobile = request.POST.get('mobile')
       password1 = request.POST.get('password1') 
       password2 = request.POST.get('password2')

       if password1 == password2:
            if User.objects.filter(username = user_name).exists():
                messages.info(request, 'Username Taken')
                return redirect('user_registration')
            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email Taken')
                return redirect('user_registration')
            else:
                user = User.objects.create_user(first_name = first_name , last_name = last_name , username=user_name, email= email , password = password1)
                user.save()
                return redirect('login')
       else:
            return redirect('user_registration')
        
       return redirect('/')

   else:
        return render(request , 'acc/user_registration.html')

def login(request):
    if request.method == "POST":
        user_name = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=user_name , password = password)

        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request , 'Invalid credentials')
            return redirect('login')
    else:
        return render(request , 'acc/login.html')


def logout(request):
    auth.logout(request)
    return redirect('/')

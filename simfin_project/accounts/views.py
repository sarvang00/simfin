from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User

from django.contrib.auth.decorators import login_required
from django.views.decorators.cache import cache_control

from banking.models import UserBankingData, UserData

def signup(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check for new username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('signup')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, 
                        password=password, 
                        email=email,
                        first_name=first_name,
                        last_name=last_name
                    )
                    #Login after register
                    #auth.login(request, user)
                    #messages.success(request, 'You are now logged in')
                    #return redirect('index')
                    
                    user.save()

                    ud = UserData(user=user)
                    ud.save()

                    ubd = UserBankingData(user=user)
                    ubd.save()

                    messages.success(request, 'You are now registered and can log in')
                    #redirect to login page to login for first time
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'user/signup.html')

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'user/login.html')

@cache_control(no_cache=True, must_revalidate=True)
@login_required(login_url='/accounts/login')
def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('login')
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

from .forms import signup

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def loginpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'incorrect username or password')

        return render(request, 'authe/login.html')

def registerpage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = signup()

        if request.method == "POST":
            form = signup(request.POST)
            if form.is_valid():
                form.save()

                user = form.cleaned_data.get('username')


                messages.success(request, 'Account created successfully for' + user)
                return redirect('login')

        context = {'form': form}
        return render(request, 'authe/register.html', context)


def logoutpage(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
def home(request):
    return render(request, 'task/home.html')
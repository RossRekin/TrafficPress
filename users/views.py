from django.shortcuts import render
from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


def login_user(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('news')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        try:
            user = User.objects.get(username=username)
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('news')
            else:
                messages.error(request,  'Невалидно име/парола.')
        except:
            messages.error(request,  'Грешка.')

    context = {'page': page}
    return render(request, 'users/login_register.html', context)


def logout_user(request):
    logout(request)
    return redirect('news')


def register_user(request):
    page = 'register'
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, 'User account was created!')

            login(request, user)
            return redirect('news')
        else:
            messages.error(request, 'An error has occured during registration')

    context = {'page': page, 'form': form}

    return render(request, 'users/login_register.html', context)

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib import messages


@login_required(login_url='login')
def base_view(request):
    return render(request, 'base.html')


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('base')
        else:
            messages.error(request, 'Login yoki parol noto‘g‘ri!')
    return render(request, 'account/login.html')


def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')

        if password1 != password2:
            messages.error(request, 'Parollar mos emas!')
            return render(request, 'account/register.html')

        if User.objects.filter(username=username).exists():
            messages.error(request, 'Bu foydalanuvchi nomi allaqachon mavjud.')
            return render(request, 'account/register.html')

        if not email:
            messages.error(request, 'Email maydoni bo‘sh bo‘lishi mumkin emas.')
            return render(request, 'account/register.html')

        if len(password1) < 7:
            messages.error(request, 'Parol kamida 7 ta belgidan iborat bo‘lishi kerak!')
            return render(request, 'account/register.html')

        user = User.objects.create_user(username=username, email=email, password=password1)

        login(request, user)
        return redirect('base')

    return render(request, 'account/register.html')


def user_logout(request):
    logout(request)
    return redirect('login')

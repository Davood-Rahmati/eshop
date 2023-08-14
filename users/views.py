from django.shortcuts import render, redirect

from .forms import UserRegistrationForm, UserLoginForm, UserCreateForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login
from .models import User
from .forms import UserUpdateForm


def user_register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd['username'])
            User.objects.create_user(cd['username'], cd['email'], cd['password'])
            messages.success(request, 'user registered successfully', 'success')
            return redirect('Home')
    else:
        form = UserRegistrationForm()
    return render(request, 'register.html', {'form': form})


def user_login(request):
    if request.method == 'POST':
        form = UserLoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, username=cd['username'], password=cd['password'])
            if user is not None:
                login(request, user)
                messages.success(request, 'logged in successfully', 'success')
                return redirect('Home')
            else:
                messages.error(request, 'username or password is wrong', 'danger')
    else:
        form = UserLoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    all = User.objects.all()
    return render(request, 'home.html', {'user:all'})


def detail(request, user_id):
    User.objects.get(id=user_id)
    return render(request, 'detail.htl', {'user': user})


def delete(request, user_id):
    User.objects.get(id=user_id).delete()
    messages.success(request, 'user deleted successfully', 'success')
    return redirect('Home')


def create(request):
    form = UserCreateForm
    return render(request, 'create.html', {'form': form})


def update(request, user_id):
    user = User.objects.get(id=user_id)
    if request.method == "POST":
        form = UserUpdateForm(request, POST, instance=user)
        if form.is_valid():
            form.save()
            messages.success(request, 'your user updated successfully', 'success')
            return redirect('detail', user_id)
    else:
        form = UserUpdateForm(instance=user)
    return render(request, "update.html", {'form': form})

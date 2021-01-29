from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
# from django.contrib.auth.views import logout     # This logout is imported from somewhere else. You can figure out where if you wanna use it.
from django.contrib.auth.decorators import login_required
# from .forms import *
from django import forms
from django.http import Http404
from django.contrib.auth.views import LogoutView
from django.template import Context
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.core.exceptions import *
# from .forms import  AddDeckForm, AddCardF

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'register.html', locals())


@login_required(login_url='/accounts/login')
def home(request):
    current_user = request.user
    # all_projects = Projects.objects.all()
    return render(request, 'index.html', locals())


@login_required(login_url='/accounts/login')
def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        # form = UploadForm()
        form = PictureUploadForm()
        my_projects = Projects.objects.filter(uploader=current_user)
        my_profile = Profile.objects.get(user_id=current_user)
    return render(request, 'profile.html', locals())

@login_required(login_url='/accounts/login')
def edit_prof(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            lol = form.save(commit=False)
            lol.uploaded_by = current_user
            lol.save()
            return redirect('profile')
    else:
        form = ProfileForm()
    return render(request, 'profile_edit.html', {'profileform': form})


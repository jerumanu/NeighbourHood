from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UpdateUserForm, UpdateUserFlashcardForm, PostForm
from django.contrib.auth import login, authenticate
from .models import Post, Flashcard
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.views.generic import RedirectView
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import authentication, permissions

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

@login_required(login_url='login')
def index(request):
    users = User.objects.exclude(id=request.user.id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.user = request.user.flashcard
            post.save()
            return HttpResponseRedirect(request.path_info)
    else:
        form = PostForm()
    params = {
        'form': form,
        'users': users,

    }
    return render(request, 'index.html', params)

@login_required(login_url='login')
def flashcard(request, username):
    # notes = request.user.flashcard.posts.all()
    if request.method == 'POST':
        user_form = UpdateUserForm(request.POST, instance=request.user)
        prof_form = UpdateUserFlashcardForm(request.POST, request.FILES, instance=request.user.flashcard)
        if user_form.is_valid() and prof_form.is_valid():
            user_form.save()
            prof_form.save()
            return HttpResponseRedirect(request.path_info)
    else:
        user_form = UpdateUserForm(instance=request.user)
        prof_form = UpdateUserFlashcardForm(instance=request.user.flashcard)
    params = {
        'user_form': user_form,
        'prof_form': prof_form,

    }
    return render(request, 'flashcard.html', params)





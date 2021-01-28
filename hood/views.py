from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm 
# from django.contrib.auth.views import logout     # This logout is imported from somewhere else. You can figure out where if you wanna use it.
from django.contrib.auth.decorators import login_required
# from .forms import *
from django.http import Http404
from django.contrib.auth.views import LogoutView

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
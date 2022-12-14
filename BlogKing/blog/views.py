from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views import generic
from .models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User


class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class UserCreationForm(forms.Form):
    Username = forms.CharField(label='Username', max_length=64)
    Password = forms.CharField(label='Password', max_length=32)


def Register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            Username = form.cleaned_data['Username']
            Password = form.cleaned_data['Password']
            #unsure if we'll use emails, so prepoulate the argument with a placeholder
            user = User.objects.create_user(Username, 'placeholder@gmail.com', Password)
            return HttpResponseRedirect('/login/')

    else:
        form = UserCreationForm()

    return render(request, 'register.html', {'form':form})

def my_login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.success(request, ("There was an error logging in, try again."))
            return HttpResponseRedirect('/login')
    else:
        return render(request,'login.html', {})

def my_logout_view(request):
	logout(request)
	messages.success(request, ("You Were Logged Out!"))
	return HttpResponseRedirect('/')
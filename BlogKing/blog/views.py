from http.client import HTTPResponse
from django.shortcuts import render, redirect
from django.views import generic
from django.views.generic import CreateView, UpdateView, DeleteView
from .models import Post
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django import forms
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from .forms import PostForm


class PostList(generic.ListView):
    def get_queryset(self):
        if(self.request.user.is_authenticated):
            return Post.objects.filter(author=self.request.user).order_by('-created_on')   
        else:
            return Post.objects.filter(status=1).order_by('-created_on')   
         
    
    template_name = 'index.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
    
class UserCreationForm(forms.Form):
    Username = forms.CharField(label='Username', max_length=64)
    Password = forms.CharField(label='Password', max_length=32)

class PostCreateForm(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'post_create.html'
    #fields = ['title', 'slug', 'content', 'status']

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(PostCreateForm, self).form_valid(form)

class PostEditForm(UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'post_edit.html'
    #fields = ['title', 'slug', 'content', 'status']

class PostDeleteForm(DeleteView):
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')



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
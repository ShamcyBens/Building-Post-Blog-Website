from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from .models import Post
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.contrib import messages
from .forms import *



def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('post_list')
        else:
            # Handle invalid login
            pass

    return render(request, 'appname/login.html')

def user_logout(request):
    logout(request)
    return redirect('post_list')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}. You can now log in.')
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'appname/register.html', {'form': form})

def view_posts(request):
    # Fetch all posts from the database
    posts = Post.objects.all()

    context = {
        'posts': posts,
    }

    return render(request, 'appname/view_posts.html', context)

def post_list(request):
    posts = Post.objects.all()
    return render(request, 'appname/post_list.html', {'posts': posts})

def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'appname/post_detail.html', {'post': post})


def send_newsletter(request):
    subject = 'Your Newsletter Subject'
    message = 'Your newsletter message content.'
    from_email = 'your@email.com'
    recipient_list = ['recipient1@example.com', 'recipient2@example.com']

    email = EmailMessage(subject, message, from_email, recipient_list)
    email.send()

def home(request):
    return render(request, 'appname/home.html')

def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save()  # Save the new post
            # Redirect to the post detail page
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm()

    return render(request, 'appname/create_posts.html', {'form': form})

def update_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('post_detail', post_id=post.id)
    else:
        form = PostForm(instance=post)

    return render(request, 'appname/update_post.html', {'form': form, 'post': post})

def delete_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    if request.method == 'POST':
        post.delete()
        return redirect('post_list')
    else:
        return render(request, 'appname/delete_post.html', {'post': post})
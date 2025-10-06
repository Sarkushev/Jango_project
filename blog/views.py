from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from .models import Post
from .forms import PostForm

def home(request):
    """Главная страница - перенаправляет на список постов"""
    return redirect('post_list')

def post_list(request):
    """Список всех постов"""
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/post_list.html', {'posts': posts})

@login_required
def create_post(request):
    """Создание поста"""
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, 'Пост успешно создан!')
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'blog/create_post.html', {'form': form})

@login_required
def edit_post(request, post_id):
    """Редактирование поста"""
    post = get_object_or_404(Post, id=post_id)
    
    if post.author != request.user:
        messages.error(request, 'Вы можете редактировать только свои посты!')
        return redirect('post_list')
    
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
            messages.success(request, 'Пост успешно обновлен!')
            return redirect('post_list')
    else:
        form = PostForm(instance=post)
    
    return render(request, 'blog/edit_post.html', {'form': form, 'post': post})

@login_required
def delete_post(request, post_id):
    """Удаление поста"""
    post = get_object_or_404(Post, id=post_id)
    
    if post.author != request.user:
        messages.error(request, 'Вы можете удалять только свои посты!')
        return redirect('post_list')
    
    if request.method == 'POST':
        post.delete()
        messages.success(request, 'Пост успешно удален!')
        return redirect('post_list')
    
    return render(request, 'blog/delete_post.html', {'post': post})

# Функция для входа (если нужно)
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f'Добро пожаловать, {username}!')
                return redirect('post_list')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})
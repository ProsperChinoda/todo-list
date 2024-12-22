from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

def welcome(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'index.html')
        else:
            messages.success(request, ("There was an error, Try again later"))
            return redirect('welcome')
   
    return render(request, 'welcome.html')

def logout_user(request):
    logout(request)
    messages.success(request, ("You successfully logged out"))
    return render(request, 'sign_up.html')

def sign_up(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        if User.objects.filter(username=username).exists():
            messages.error(request, ("Username already exists, Please try another one"))
            return redirect('sign_up')
        else:
            user = User.objects.create_user(username=username, email=email,password=password)
            user.save()
            return redirect('welcome')
        
    return render(request, 'sign_up.html')

def index(request):
    if request.method == 'POST':
        card = request.POST['title']
        desc = request.POST['desc']
        colour = request.POST['color']
        user = request.user
        print(card, desc, colour, user)
        task = TODO(title=card, desc=desc, color=colour, user=request.user)
        task.save()
        result = TODO.objects.all()
        return render(request, 'index.html', {'result': result})

    result = TODO.objects.all()
    return render(request, 'index.html', {'result': result})

def edit_todo(request, id):
    if request.method == 'POST':
        card = request.POST['title']
        desc = request.POST['desc']
        colour = request.POST['color']
        obj = TODO.objects.get(id=id)
        obj.title = card
        obj.desc = desc
        obj.color = colour
        obj.save()
        return redirect('index')
    
    item = TODO.objects.get(id=id)
    return render(request, 'edit.html', {'term':item})

def delete_todo(request, id):
    obj = TODO.objects.get(id=id)
    obj.delete()
    return redirect('index')
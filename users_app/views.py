from django.shortcuts import render, redirect, HttpResponse
from .models import Users


def index(request):
    users= Users.objects.all()
    context= {
    "users": users
    }
    return render(request, 'index.html', context)


def show(request):
    return redirect('/')


def submit (request):
    first_name=request.POST['first_name']
    last_name=request.POST['last_name']
    email=request.POST['email']
    age=request.POST['age']

    u1 = Users.objects.create(first_name=first_name, last_name=last_name, email=email, age=age)

    return redirect('/show')


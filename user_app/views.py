from django.shortcuts import render, HttpResponse, redirect
from .models import User
# Create your views here.

def index(request):
    context = {
    "all_the_users": User.objects.all()
    }
    return render(request, 'index.html', context)

def create_user(request):
    if request.method == 'POST':
        users = User()
        users.first_name = request.POST.get('firstname')
        users.last_name = request.POST.get('lastname')
        users.email_address = request.POST.get('email')
        users.age = request.POST.get('age')
        users.save()

    return redirect('/')
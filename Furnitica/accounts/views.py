from django.shortcuts import render

# Create your views here.

def account(request):
    return render(request, 'user-acount.html')

def login(request):
    return render(request, 'user-login.html')

def register(request):
    return render(request, 'user-register.html')

def resert_password(request):
    return render(request, 'user-reset-password.html')






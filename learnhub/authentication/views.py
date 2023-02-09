from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.views.generic import View
from .models import User
from django.contrib import messages
# Create your views here.


class Registeration(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        form = UserRegistrationForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if not User.objects.filter(username=username).exists():
                if not User.objects.filter(email=email).exists():
                    if len(password) < 8:
                        messages.error(request, 'password is too short')
                        return render(request, 'authentication/register.html', {'form': form})

            user = form.save()
            messages.success(request, f'account created for {user.username}.')
        return render(request, 'authentication/register.html', {'form': form})

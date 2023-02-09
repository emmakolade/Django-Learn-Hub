from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import UserRegistrationForm
from django.views.generic import View
from .models import UserProfile
from django.contrib import messages
# Create your views here.


class Registeration(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password2 = form.cleaned_data.get('password2')
            
            UserProfile.objects.create(
                user=user, username=username, email=email)
            messages.success(request, f'account created for {username}.')
            return redirect('login')
        context = {'form': form}
        return render(request, 'authentication/register.html', context)

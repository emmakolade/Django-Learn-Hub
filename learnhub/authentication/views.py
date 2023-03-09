from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
from .forms import UserRegistrationForm, PasswordChangeForm, EditProfileForm
from django.views.generic import View
from .models import User, UserProfile
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required


# RESIGRATION AND LOGIN VIEW
class Registeration(View):
    def get(self, request):
        return render(request, 'authentication/register.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('base')
        else:
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
                UserProfile.objects.create(user=user)
                messages.success(
                    request, f'account created for {user.username}.')
                return redirect('login')
            return render(request, 'authentication/register.html', {'form': form})


class UsernameValidation(View):
    pass


class Login(View):
    def get(self, request):
        return render(request, 'authentication/login.html')

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('base')
        else:
            username = request.POST.get('username')
            password = request.POST.get('password')
            if username and password:
                user = authenticate(
                    request, username=username, password=password)

                if user is not None:
                    login(request, user)
                    messages.success(
                        request, f'welcome <b>{username}<b>, you are now logged in')
                    return redirect('base')
                messages.error(request, 'invalid credentials, try again')
            else:
                messages.error(request, 'please fill all fields')

            return render(request, 'authentication/login.html')


class Logout(View):
    def get(self, request):
        logout(request)
        messages.success(request, 'you have been logged out')
        return redirect('base')


# PASSWORD CHANGE AND PASSWORD DONE
class UserPasswordChangeView(LoginRequiredMixin, PasswordChangeView):
    login_url = '/authentication/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'authentication/password_change_form.html'
    form_class = PasswordChangeForm
    success_url = '/authentication/password_done/'


password_change = UserPasswordChangeView.as_view()


class UserPasswordChangeDoneView(LoginRequiredMixin, PasswordChangeDoneView):
    login_url = '/authentication/login/'
    redirect_field_name = 'redirect_to'
    template_name = 'authentication/password_change_done.html'


password_done = UserPasswordChangeDoneView.as_view()

# TODO: PASSWORD RESET AND EMAIL VERIFICATION
class PasswordReset(View):
    pass


class EmailVerification(View):
    pass




# USER PROFILE
def user_profile(request):
    if request.user.is_authenticated:
        profile = request.user.userprofile
        context = {
            'profile': profile,
        }
        return render(request, 'authentication/user_profile.html', context)
    else:
        messages.info(request, 'you need to login to access your profile')
        return redirect('login')


@ login_required
def edit_profile(request):
    profile = request.user.userprofile
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=profile)
        if form.is_valid():
            form.save()
            messages.success(request, 'profile updated succesfully')
            return redirect('user_profile')
    else:
        form = EditProfileForm(instance=profile)

    context = {
        'form': form,
    }
    return render(request, 'authentication/edit_profile.html', context)


@login_required
def delete_profile(request):
    user = request.user
    if request.method=='POST':
        user.delete()
        logout(request)
        messages.info(request, 'account deleted successfully')
        return redirect('base')
    return render(request, 'authentication/delete_profile.html')
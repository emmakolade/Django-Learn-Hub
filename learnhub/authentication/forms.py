from django import forms
from .models import User, UserProfile
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm


# USER REGISTRATION FORM
class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    password2 = forms.CharField(
        widget=forms.PasswordInput, label='confirm password')

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Passwords don't match")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user

# class UserLoginForm(AuthenticationForm)


class PasswordChangeForm(PasswordChangeForm):
    pass


# EDIT PROFILE FORM
class EditProfileForm(forms.ModelForm):
    vid_quality = forms.ChoiceField(choices=UserProfile.VIDEO_QUALITY)

    class Meta:
        model = UserProfile
        fields = ['bio', 'vid_quality']

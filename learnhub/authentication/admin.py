from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, UserProfile
# Register your models here.


class CustomUserAdmin(UserAdmin):
    model = User
    list_display = ["username", "email", "last_login",
                    "date_joined"]


admin.site.register(User, CustomUserAdmin)
admin.site.register(UserProfile)

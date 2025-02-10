from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser
from .forms import CustomUserCreationForm, CustomUserChangeForm
from accounts.models import CustomUser

class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomUser
    list_display = ("name","username", "email",'is_staff')

    fieldsets = (
        (None, {'fields': ('username', 'email', 'password')}),
        ('Personal info', {'fields': ('name',)}),  # Campo personalizado
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('name','username', 'email', 'password1', 'password2'),
        }),
    )

admin.site.register(CustomUser, CustomUserAdmin)

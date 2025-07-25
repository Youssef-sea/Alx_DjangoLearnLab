# advanced_features_and_security/accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser

class CustomUserAdmin(UserAdmin):
    # The fields to be displayed in the list view of the admin
    list_display = ('email', 'first_name', 'last_name', 'is_staff', 'date_of_birth')

    # Fields to be used when adding a new user in the admin
    add_fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Fields to be used when changing an existing user in the admin
    fieldsets = (
        (None, {'fields': ('email',)}), # Email is now the primary identifier
        ('Personal info', {'fields': ('first_name', 'last_name', 'date_of_birth', 'profile_photo')}),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')}),
        ('Important dates', {'fields': ('last_login', 'date_joined')}),
    )

    # Make 'email' the field used for searching
    search_fields = ('email',)
    ordering = ('email',)

    # Exclude username as we are not using it
    filter_horizontal = ('groups', 'user_permissions',)

admin.site.register(CustomUser, CustomUserAdmin)
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import User

@admin.register(User)
class UserAdmin(BaseUserAdmin):
    fieldsets = BaseUserAdmin.fieldsets + (
        ('Información adicional', {'fields': ('pais',)}),
    )
    list_display = ('username', 'email', 'first_name', 'last_name', 'pais', 'is_staff')
    list_filter = ('pais', 'is_staff', 'is_superuser')

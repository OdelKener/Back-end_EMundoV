from django.contrib import admin


from django.contrib.auth.admin import UserAdmin

from App.Seguridad.Usuario.models import User

@admin.register(User)
class UserAdmin(UserAdmin):
    pass

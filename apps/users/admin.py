from django.contrib import admin
# Register your models here.
from django.contrib.auth.admin import UserAdmin
from apps.users.models import User

#mediante esta funcion agregamos los campos adicionales del useradmin
class MyUserAdmin(UserAdmin):
    model = User
    fieldsets = UserAdmin.fieldsets + (
            (None, {'fields': ('celular','vendedor')}),
    )

admin.site.register(User,MyUserAdmin)

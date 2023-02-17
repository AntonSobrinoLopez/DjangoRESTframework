from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    fieldsets = [
        ("Login", {'fields': ['id','username', 'password']}),
        ('Datos Personales', {'fields': ['firstname', 'lastname']}),
        ('Datos de Contacto', {'fields': ['email', 'address', 'phone']}),
    ]

admin.site.register(User,UserAdmin)
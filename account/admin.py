from django.contrib import admin
from .models import Userregistration

# Register your models here.
@admin.register(Userregistration)
class UserregAdmin(admin.ModelAdmin):
    list_display = ["id", "username","email", "mobile", "password"]
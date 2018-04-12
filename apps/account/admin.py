from django.contrib import admin
from django.db import models
from .models import User
# Register your models here.

class Display(admin.ModelAdmin):
    list_display = ('username', 'email')

admin.site.register(User, Display)
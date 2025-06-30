from django.contrib import admin

# Register your models here.
from .forms import CustomUserCreationForm,CustomUserChangeForm
from .models import User,Message


admin.site.register(User)
admin.site.register(Message)

from django.contrib import admin
from .models import UserModel

# Register your models here.

admin.site.register(UserModel)  # UserModel을 Admin에 추가
from django.contrib import admin
from users.models.customuser import CustomUser

admin.site.register(CustomUser)

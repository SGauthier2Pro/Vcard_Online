from django.contrib import admin
from users.models.customuser import CustomUser
from users.models.address import Address

admin.site.register(CustomUser)
admin.site.register(Address)

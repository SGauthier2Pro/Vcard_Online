from django.contrib import admin
from cv.models.cv import Cv
from cv.models.experience import Experience

admin.site.register(Cv)
admin.site.register(Experience)

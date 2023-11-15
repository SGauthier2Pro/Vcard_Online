from django.contrib import admin
from cv.models.cv import Cv
from cv.models.experience import Experience
from cv.models.hobbies import Hobbies
from cv.models.formation import Formation

admin.site.register(Cv)
admin.site.register(Experience)
admin.site.register(Hobbies)
admin.site.register(Formation)


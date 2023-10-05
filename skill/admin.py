from django.contrib import admin
from skill.models.technology import Technology
from skill.models.softskill import SoftSkill
from skill.models.language import Language


admin.site.register(Technology)
admin.site.register(SoftSkill)
admin.site.register(Language)

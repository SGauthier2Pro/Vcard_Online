from django.urls import path

import skill.views.technology_views
import skill.views.softskill_views
import skill.views.language_views
import skill.views.home_view

app_name = 'skill'

urlpatterns = [
    path('', skill.views.home_view.index, name='skill_home'),
    path('technology/', skill.views.technology_views.index, name='technology_home'),
    path('technology/create/', skill.views.technology_views.create_technology,
         name='create_technology'),
    path('technology/<int:technology_id>/delete/', skill.views.technology_views.delete_technology,
         name='delete_technology'),
    path('technology/<int:technology_id>/edit/', skill.views.technology_views.edit_technology,
         name='edit_technology'),
    path('softskill/', skill.views.softskill_views.index, name='softskill_home'),
    path('softskill/create/', skill.views.softskill_views.create_softskill,
         name='create_softskill'),
    path('softskill/<int:softskill_id>/delete/', skill.views.softskill_views.delete_softskill,
         name='delete_softskill'),
    path('softskill/<int:softskill_id>/edit/', skill.views.softskill_views.edit_softskill,
         name='edit_softskill'),
    path('language/', skill.views.language_views.index, name='language_home'),
    path('language/create/', skill.views.language_views.create_language,
         name='create_language'),
    path('language/<int:language_id>/delete/', skill.views.language_views.delete_language,
         name='delete_language'),
    path('language/<int:language_id>/edit/', skill.views.language_views.edit_language,
         name='edit_language')

]

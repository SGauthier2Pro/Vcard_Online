from django.urls import path

import skill.views.technology_views

app_name = 'skill'

urlpatterns = [
    path('technology/', skill.views.technology_views.index, name='technology_home'),
    path('technology/create/', skill.views.technology_views.create_technology,
         name='create_technology'),
    path('technology/<int:technology_id>/delete/', skill.views.technology_views.delete_technology,
         name='delete_technology'),
    path('technology/<int:technology_id>/edit/', skill.views.technology_views.edit_technology,
         name='edit_technology')

]

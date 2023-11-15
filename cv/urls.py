from django.urls import path

from cv.views import cv_views, hobbies_views, formation_views, experience_views, about_views, contact_views

app_name = 'cv'

urlpatterns = [
    path('', cv_views.index, name='cv_home'),
    path('about/<str:access_code>/', about_views.about, name='about'),
    path('contact/<str:access_code>/', contact_views.contact, name='contact'),
    path('<int:cv_id>/', cv_views.show_cv, name='display_cv'),
    path('<int:cv_id>/print_CV/', cv_views.print_cv, name='print_cv'),
    path('<int:cv_id>/edit/', cv_views.edit_cv, name='edit_cv'),
    path('<int:cv_id>/delete/', cv_views.delete_cv, name='delete_cv'),
    path('create/', cv_views.create_cv, name='create_cv'),
    path('experience/', experience_views.index, name='experience_home'),
    path('experience/create/', experience_views.create_experience,
         name='create_experience'),
    path('experience/<int:experience_id>/delete/', experience_views.delete_experience,
         name='delete_experience'),
    path('experience/<int:experience_id>/edit/', experience_views.edit_experience,
         name='edit_experience'),
    path('formation/', formation_views.index, name='formation_home'),
    path('formation/create/', formation_views.create_formation,
         name='create_formation'),
    path('formation/<int:formation_id>/delete/', formation_views.delete_formation,
         name='delete_formation'),
    path('formation/<int:formation_id>/edit/', formation_views.edit_formation,
         name='edit_formation'),
    path('hobbies/', hobbies_views.index, name='hobbies_home'),
    path('hobbies/create/', hobbies_views.create_hobbies,
         name='create_hobbies'),
    path('hobbies/<int:hobbies_id>/delete/', hobbies_views.delete_hobbies,
         name='delete_hobbies'),
    path('hobbies/<int:hobbies_id>/edit/', hobbies_views.edit_hobbies,
         name='edit_hobbies')
]

from django.urls import path

from project.views import project_views

app_name = 'project'

urlpatterns = [
    path('', project_views.index, name='project_home'),
    path('<int:project_id>/', project_views.show_project, name='display_project'),
    path('<int:project_id>/edit/', project_views.edit_project, name='edit_project'),
    path('<int:project_id>/delete/', project_views.delete_project, name='delete_project'),
    path('create/', project_views.create_project, name='create_project'),
]

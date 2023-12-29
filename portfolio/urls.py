from django.urls import path
from portfolio.views import contact_views, index_views, projects_views, portfolio_views

app_name = 'portfolio'

urlpatterns = [
    path('', portfolio_views.index, name='portfolio_home'),
    path('test/<int:portfolio_id>/', portfolio_views.set_portfolio_visible,
         name='set_portfolio_visible'),
    path('<int:portfolio_id>/edit/', portfolio_views.edit_portfolio, name='edit_portfolio'),
    path('<int:portfolio_id>/delete/', portfolio_views.delete_portfolio, name='delete_portfolio'),
    path('create/', portfolio_views.create_portfolio, name='create_portfolio'),
    path('<str:access_code>/', index_views.index_invited, name='portfolio'),
    path('contact/<str:access_code>/', contact_views.contact, name='contact'),
    path('projects/<int:project_id>/<str:access_code>/', projects_views.show_project,
         name='display_project'),
]

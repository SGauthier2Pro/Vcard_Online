"""
URL configuration for vcardonline project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.static import serve
from django.conf import settings
from django.conf.urls.static import static
from .views.index import index, access_code

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('access-code/', access_code, name='access_code'),
    path(r'users/', include('users.urls', namespace='users')),
    path(r'project/', include('project.urls', namespace='project')),
    path(r'cv/', include('cv.urls', namespace='cv')),
    path(r'skill/', include('skill.urls', namespace='skill')),
    path(r'portfolio/', include('portfolio.urls', namespace='portfolio')),
    re_path(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

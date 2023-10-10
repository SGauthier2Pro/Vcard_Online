from django.shortcuts import render


def index(request):
    return render(request, 'projects_index.html')

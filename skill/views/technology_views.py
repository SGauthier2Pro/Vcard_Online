from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from skill.models.technology import Technology
from skill.forms import technologyform


@login_required
def index(request):
    technologies = Technology.objects.filter(
        Q(user=request.user)
    )

    return render(request,
                  'skill/technologies_index.html',
                  context={'technologies': technologies}
                  )


@login_required
def create_technology(request):
    technology_form = technologyform.TechnologyForm()
    if request.method == 'POST':
        technology_form = technologyform.TechnologyForm(request.POST, request.FILES)
        if technology_form.is_valid():
            technology_to_save = technology_form.save(commit=False)
            technology_to_save.user = request.user
            technology_to_save.save()
            return redirect('skill:technology_home')
    return render(request,
                  'skill/create_technology.html',
                  context={'technology_form': technology_form}
                  )


@login_required
def edit_technology(request, technology_id):
    technology = get_object_or_404(Technology,
                                   id=technology_id)
    edit_form = technologyform.TechnologyForm(instance=technology)
    if request.method == 'POST':
        edit_form = technologyform.TechnologyForm(request.POST,
                                                  request.FILES,
                                                  instance=technology)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('skill:technology_home')
    context = {
        'technology': technology,
        'edit_form': edit_form,
    }
    return render(request,
                  'skill/edit_technology.html',
                  context=context)


@login_required
def delete_technology(request, technology_id):
    technology = get_object_or_404(Technology, id=technology_id)
    delete_form = technologyform.DeleteTechnologyForm()
    if request.method == 'POST':
        delete_form = technologyform.DeleteTechnologyForm(request.POST)
        if delete_form.is_valid():
            technology.delete()
            return redirect('skill:technology_home')
    context = {
        'technology': technology,
        'delete_form': delete_form,
    }
    return render(request,
                  'skill/delete_technology.html',
                  context=context)

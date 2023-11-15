from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from cv.models.experience import Experience
from cv.forms import experienceform


@login_required
def index(request):
    experiences = Experience.objects.filter(
        Q(user=request.user)
    )

    return render(request,
                  'cv/experiences_index.html',
                  context={'experiences': experiences}
                  )


@login_required
def create_experience(request):
    experience_form = experienceform.ExperienceForm()
    if request.method == 'POST':
        experience_form = experienceform.ExperienceForm(request.POST)
        if experience_form.is_valid():
            experience_to_save = experience_form.save(commit=False)
            experience_to_save.user = request.user
            experience_to_save.save()
            return redirect('cv:experience_home')
    return render(request,
                  'cv/create_experience.html',
                  context={'experience_form': experience_form}
                  )


@login_required
def edit_experience(request, experience_id):
    experience = get_object_or_404(Experience,
                                   id=experience_id)
    edit_form = experienceform.ExperienceForm(instance=experience)
    if request.method == 'POST':
        edit_form = experienceform.ExperienceForm(request.POST,
                                                  instance=experience)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('cv:experience_home')
    context = {
        'experience': experience,
        'edit_form': edit_form,
    }
    return render(request,
                  'cv/edit_experience.html',
                  context=context)


@login_required
def delete_experience(request, experience_id):
    experience = get_object_or_404(Experience, id=experience_id)
    delete_form = experienceform.DeleteExperienceForm()
    if request.method == 'POST':
        delete_form = experienceform.DeleteExperienceForm(request.POST)
        if delete_form.is_valid():
            experience.delete()
            return redirect('cv:experience_home')
    context = {
        'experience': experience,
        'delete_form': delete_form,
    }
    return render(request,
                  'cv/delete_experience.html',
                  context=context)

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from skill.models.softskill import SoftSkill
from skill.forms import softskillform


@login_required
def index(request):
    softskills = SoftSkill.objects.filter(
        Q(user=request.user)
    )

    return render(request,
                  'skill/softskills_index.html',
                  context={'softskills': softskills}
                  )


@login_required
def create_softskill(request):
    softskill_form = softskillform.SoftSkillForm()
    if request.method == 'POST':
        softskill_form = softskillform.SoftSkillForm(request.POST)
        if softskill_form.is_valid():
            softskill_to_save = softskill_form.save(commit=False)
            softskill_to_save.user = request.user
            softskill_to_save.save()
            return redirect('skill:softskill_home')
    return render(request,
                  'skill/create_softskill.html',
                  context={'softskill_form': softskill_form}
                  )


@login_required
def edit_softskill(request, softskill_id):
    softskill = get_object_or_404(SoftSkill,
                                  id=softskill_id)
    edit_form = softskillform.SoftSkillForm(instance=softskill)
    if request.method == 'POST':
        edit_form = softskillform.SoftSkillForm(request.POST,
                                                instance=softskill)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('skill:softskill_home')
    context = {
        'softskill': softskill,
        'edit_form': edit_form,
    }
    return render(request,
                  'skill/edit_softskill.html',
                  context=context)


@login_required
def delete_softskill(request, softskill_id):
    softskill = get_object_or_404(SoftSkill, id=softskill_id)
    delete_form = softskillform.DeleteSoftSkillForm()
    if request.method == 'POST':
        delete_form = softskillform.DeleteSoftSkillForm(request.POST)
        if delete_form.is_valid():
            softskill.delete()
            return redirect('skill:softskill_home')
    context = {
        'softskill': softskill,
        'delete_form': delete_form,
    }
    return render(request,
                  'skill/delete_softskill.html',
                  context=context)

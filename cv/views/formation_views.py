from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from cv.models.formation import Formation
from cv.forms import formationform


@login_required
def index(request):
    formations = Formation.objects.filter(
        Q(user=request.user)
    )

    return render(request,
                  'cv/formations_index.html',
                  context={'formations': formations}
                  )


@login_required
def create_formation(request):
    formation_form = formationform.FormationForm()
    if request.method == 'POST':
        formation_form = formationform.FormationForm(request.POST, request.FILES)
        if formation_form.is_valid():
            formation_to_save = formation_form.save(commit=False)
            formation_to_save.user = request.user
            formation_to_save.save()
            return redirect('cv:formation_home')
    return render(request,
                  'cv/create_formation.html',
                  context={'formation_form': formation_form}
                  )


@login_required
def edit_formation(request, formation_id):
    formation = get_object_or_404(Formation,
                                  id=formation_id)
    edit_form = formationform.FormationForm(instance=formation)
    if request.method == 'POST':
        edit_form = formationform.FormationForm(request.POST,
                                                request.FILES,
                                                instance=formation)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('cv:formation_home')
    context = {
        'formation': formation,
        'edit_form': edit_form,
    }
    return render(request,
                  'cv/edit_formation.html',
                  context=context)


@login_required
def delete_formation(request, formation_id):
    formation = get_object_or_404(Formation, id=formation_id)
    delete_form = formationform.DeleteFormationForm()
    if request.method == 'POST':
        delete_form = formationform.DeleteFormationForm(request.POST)
        if delete_form.is_valid():
            formation.delete()
            return redirect('cv:formation_home')
    context = {
        'formation': formation,
        'delete_form': delete_form,
    }
    return render(request,
                  'cv/delete_formation.html',
                  context=context)

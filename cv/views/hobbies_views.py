from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from cv.models.hobbies import Hobbies
from cv.forms import hobbiesform


@login_required
def index(request):
    hobbies = Hobbies.objects.filter(
        Q(user=request.user)
    )

    return render(request,
                  'cv/hobbies_index.html',
                  context={'hobbies': hobbies}
                  )


@login_required
def create_hobbies(request):
    hobbies_form = hobbiesform.HobbiesForm()
    if request.method == 'POST':
        hobbies_form = hobbiesform.HobbiesForm(request.POST)
        if hobbies_form.is_valid():
            hobbies_to_save = hobbies_form.save(commit=False)
            hobbies_to_save.user = request.user
            hobbies_to_save.save()
            return redirect('cv:hobbies_home')
    return render(request,
                  'cv/create_hobbies.html',
                  context={'hobbies_form': hobbies_form}
                  )


@login_required
def edit_hobbies(request, hobbies_id):
    hobbies = get_object_or_404(Hobbies,
                                id=hobbies_id)
    edit_form = hobbiesform.HobbiesForm(instance=hobbies)
    if request.method == 'POST':
        edit_form = hobbiesform.HobbiesForm(request.POST,
                                            instance=hobbies)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('cv:hobbies_home')
    context = {
        'hobbies': hobbies,
        'edit_form': edit_form,
    }
    return render(request,
                  'cv/edit_hobbies.html',
                  context=context)


@login_required
def delete_hobbies(request, hobbies_id):
    hobbies = get_object_or_404(Hobbies, id=hobbies_id)
    delete_form = hobbiesform.DeleteHobbiesForm()
    if request.method == 'POST':
        delete_form = hobbiesform.DeleteHobbiesForm(request.POST)
        if delete_form.is_valid():
            hobbies.delete()
            return redirect('cv:hobbies_home')
    context = {
        'hobbies': hobbies,
        'delete_form': delete_form,
    }
    return render(request,
                  'cv/delete_hobbies.html',
                  context=context)

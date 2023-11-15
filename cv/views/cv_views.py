from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from users.models.customuser import CustomUser

from cv.models.cv import Cv
from cv.forms import cvform


@login_required
def index(request):
    cvs = Cv.objects.filter(
        Q(user=request.user)
    )

    return render(request,
                  'cv/cvs_index.html',
                  context={'cvs': cvs}
                  )


def invited_cv(request, access_code):
    if CustomUser.objects.filter(guest_access_code=access_code):
        user_inviter = CustomUser.objects.get(guest_access_code=access_code)
        user_inviter.reset_guest_access_code()
        if user_inviter.guest_access_code:
            cv = get_object_or_404(Cv,
                                   user=user_inviter,
                                   can_be_display=True)
            return render(request,
                          'cv/cv.html',
                          context={'cv': cv,
                                   'access_code': access_code,
                                   'inviter': user_inviter}
                          )


def print_cv(request, cv_id):
    cv = Cv.objects.get(id=cv_id)

    return render(request,
                  'cv/printable_cv.html',
                  context={'cv': cv})

@login_required
def show_cv(request, cv_id):
    cv = get_object_or_404(Cv,
                           id=cv_id)
    return render(request,
                  'cv/cv.html',
                  context={'cv': cv}
                  )


@login_required
def create_cv(request):
    cv_form = cvform.CvForm(request.user)
    if request.method == 'POST':
        cv_form = cvform.CvForm(request.user, request.POST)
        if cv_form.is_valid():
            cv_to_save = cv_form.save(commit=False)
            cv_to_save.user = request.user
            cv_to_save.save()
            cv_form.save_m2m()  # Save the many-to-many field
            return redirect('cv:cv_home')
    return render(request,
                  'cv/create_cv.html',
                  context={'cv_form': cv_form}
                  )


@login_required
def edit_cv(request, cv_id):
    cv = get_object_or_404(Cv,
                           id=cv_id)
    edit_form = cvform.CvForm(user=request.user, instance=cv)
    if request.method == 'POST':
        edit_form = cvform.CvForm(user=request.user,
                                  data=request.POST,
                                  instance=cv)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('cv:cv_home')
    context = {
        'cv': cv,
        'edit_form': edit_form,
    }
    return render(request,
                  'cv/edit_cv.html',
                  context=context)


@login_required
def delete_cv(request, cv_id):
    cv = get_object_or_404(Cv, id=cv_id)
    delete_form = cvform.DeleteCvForm()
    if request.method == 'POST':
        delete_form = cvform.DeleteCvForm(request.POST)
        if delete_form.is_valid():
            cv.delete()
            return redirect('cv:cv_home')
    context = {
        'cv': cv,
        'delete_form': delete_form,
    }
    return render(request,
                  'cv/delete_cv.html',
                  context=context)


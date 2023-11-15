from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from users.forms.profileform import ProfileForm
from users.models.customuser import CustomUser


@login_required
def index(request):

    return render(request,
                  'users/profile.html',
                  context={'user': request.user}
                  )


@login_required
def edit_profile(request):
    form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('users:profile_home')
    return render(request, 'users/edit_profile_form.html', context={'form': form})


@login_required
def generate_guest_access_code(request):
    try:
        user = CustomUser.objects.get(id=request.user.id)
        user.generate_guest_access_code()
        user.save()
        messages.success(request, 'Votre code d\'accès invité a été créé avec succès.')
    except ValueError:
        messages.error(request, 'L\'utilisateur spécifié n\'existe pas.')
    return redirect('users:profile_home')

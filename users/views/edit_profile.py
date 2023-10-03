from django.shortcuts import redirect, render

from users.forms.profileform import ProfileForm


def edit_profile(request):
    form = ProfileForm(instance=request.user)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('index')
    return render(request, 'users/edit_profile_form.html', context={'form': form})

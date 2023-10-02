from django.shortcuts import redirect, render

from users.forms.uploadprofilephotoform import UploadProfilePhotoForm


def upload_profile_photo(request):
    form = UploadProfilePhotoForm(instance=request.user)
    if request.method == 'POST':
        form = UploadProfilePhotoForm(request.POST, request.FILES, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('home')
    return render(request, 'users/upload_profile_photo.html', context={'form': form})

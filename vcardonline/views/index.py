from django.shortcuts import render, redirect
from users.models.customuser import CustomUser

from vcardonline.forms.accesscodeform import AccessCodeForm


def index(request):
    return render(request, 'index.html')


def access_code(request):
    form = AccessCodeForm()
    if request.method == "POST":
        form = AccessCodeForm(request.POST)
        if form.is_valid():
            access_code_value = form.cleaned_data['access_code_invited']
            if CustomUser.objects.filter(guest_access_code=access_code_value):
                return redirect('portfolio:portfolio',
                                access_code=access_code_value
                                )
            else:
                return render(request,
                              'access_denied.html',
                              context={
                                  'message': "Le code que vous utilisez n'est pas valide !"
                              })
    return render(request,
                  'access_code_form.html',
                  context={'form': form},
                  )

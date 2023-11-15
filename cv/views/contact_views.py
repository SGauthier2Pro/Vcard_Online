from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.core.mail import send_mail
from users.models.customuser import CustomUser
from cv.models.cv import Cv


def contact(request, access_code):
    if CustomUser.objects.filter(guest_access_code=access_code):
        user_inviter = CustomUser.objects.get(guest_access_code=access_code)
        user_inviter.reset_guest_access_code()
        if user_inviter.guest_access_code:
            cv = get_object_or_404(Cv,
                                   user=user_inviter,
                                   can_be_display=True)
            if request.method == 'POST':
                name = request.POST.get('name', '')
                email = request.POST.get('email', '')
                message = request.POST.get('message', '')

                send_mail(
                    f'Nouveau message du contact {name}',
                    message,
                    email,
                    [f'{cv.user.email}'],
                    fail_silently=False,
                )

                return HttpResponseRedirect(
                    'index')

            return render(request,
                          'cv/contact.html',
                          context={'cv': cv,
                                   'access_code': access_code,
                                   'inviter': user_inviter}
                          )


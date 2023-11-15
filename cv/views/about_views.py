from users.models.customuser import CustomUser
from cv.models.cv import Cv
from django.shortcuts import render, get_object_or_404


def about(request, access_code):
    if CustomUser.objects.filter(guest_access_code=access_code):
        user_inviter = CustomUser.objects.get(guest_access_code=access_code)
        user_inviter.reset_guest_access_code()
        if user_inviter.guest_access_code:
            cv = get_object_or_404(Cv,
                                   user=user_inviter,
                                   can_be_display=True)
            return render(request,
                          'cv/about.html',
                          context={'cv': cv,
                                   'access_code': access_code,
                                   'inviter': user_inviter}
                          )
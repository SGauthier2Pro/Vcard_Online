from django.db.models import Q
from django.shortcuts import render, get_object_or_404

from users.models.customuser import CustomUser
from project.models.project import Project
from portfolio.models.portfolio import Portfolio
from cv.models.cv import Cv


def index_invited(request, access_code):
    if CustomUser.objects.filter(guest_access_code=access_code):
        user_inviter = CustomUser.objects.get(guest_access_code=access_code)
        user_inviter.reset_guest_access_code()
        if user_inviter.guest_access_code:
            projects = Project.objects.filter(
                Q(user=user_inviter),
                Q(can_be_display=True)
            )

            cv = get_object_or_404(Cv,
                                   user=user_inviter,
                                   can_be_display=True)

            portfolio = get_object_or_404(Portfolio,
                                          user=user_inviter,
                                          is_visible=True)

            return render(request,
                          'portfolio/index.html',
                          context={
                              'access_code': access_code,
                              'inviter': user_inviter,
                              'projects': projects,
                              'cv': cv,
                              'portfolio': portfolio
                          }
                          )
        else:
            return render(request,
                          'project/access_denied.html',
                          context={
                              'message': "Le code que vous utilisez n'est pas valide !"
                          })
    else:
        return render(request,
                      'project/access_denied.html',
                      context={
                          'message': "Le code invité que vous utilisez n'est pas valide !"
                      })
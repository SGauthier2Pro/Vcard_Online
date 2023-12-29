from django.shortcuts import render

from project.models.project import Project
from users.models.customuser import CustomUser


def show_project(request, project_id, access_code):
    if CustomUser.objects.filter(guest_access_code=access_code):
        user_inviter = CustomUser.objects.get(guest_access_code=access_code)
        user_inviter.reset_guest_access_code()
        if Project.objects.filter(id=project_id):
            project = Project.objects.get(id=project_id)
            return render(request,
                          'project/project.html',
                          context={
                              'project': project,
                              'access_code': access_code,
                              'inviter': user_inviter
                                   }
                          )
        else:
            return render(request,
                          'project/access_denied.html',
                          context={
                              'message': "Le code projet n'est pas valide !"
                          })
    else:
        return render(request,
                      'project/access_denied.html',
                      context={
                          'message': "Le code invité n'est pas valide !"
                      })


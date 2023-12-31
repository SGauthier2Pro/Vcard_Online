from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from project.models.project import Project
from project.forms import projectform
from users.models.customuser import CustomUser
from skill.models.technology import Technology
from skill.models.softskill import SoftSkill

@login_required
def index(request):
    projects = Project.objects.filter(
        Q(user=request.user)
    )

    return render(request,
                  'project/projects_index.html',
                  context={'projects': projects}
                  )


def index_invited(request, access_code):
    if CustomUser.objects.filter(guest_access_code=access_code):
        user_inviter = CustomUser.objects.get(guest_access_code=access_code)
        user_inviter.reset_guest_access_code()
        if user_inviter.guest_access_code:
            projects = Project.objects.filter(
                Q(user=user_inviter)
            )

            return render(request,
                          'project/projects_index.html',
                          context={'projects': projects,
                                   'access_code': access_code,
                                   'inviter': user_inviter}
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


@login_required
def show_project(request, project_id):
    if Project.objects.filter(id=project_id):
        project = Project.objects.get(id=project_id)
        return render(request,
                      'project/project.html',
                      context={
                          'project': project
                               }
                      )
    else:
        return render(request,
                      'project/access_denied.html',
                      context={
                          'message': "Le code projet n'est pas valide !"
                      })


"""def show_project_invited(request, project_id, access_code):
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
"""

@login_required
def create_project(request):
    technologies_divider = int(Technology.objects.filter(user=request.user).count() / 4) + 1
    softskills_divider = int(SoftSkill.objects.filter(user=request.user).count() / 4) + 1
    project_form = projectform.ProjectForm(request.user)
    if request.method == 'POST':
        project_form = projectform.ProjectForm(request.user, request.POST, request.FILES)
        if project_form.is_valid():
            project_to_save = project_form.save(commit=False)
            project_to_save.user = request.user
            project_to_save.save()
            project_form.save_m2m()  # Save the many-to-many field
            return redirect('project:project_home')
    return render(request,
                  'project/create_project.html',
                  context={
                      'project_form': project_form,
                      'softskills_divider': softskills_divider,
                      'technologies_divider': technologies_divider
                  }
                  )


@login_required
def edit_project(request, project_id):
    technologies_divider = int(Technology.objects.filter(user=request.user).count() / 4) + 1
    softskills_divider = int(SoftSkill.objects.filter(user=request.user).count() / 4) + 1
    project = get_object_or_404(Project,
                                id=project_id)
    edit_form = projectform.ProjectForm(user=request.user, instance=project)
    if request.method == 'POST':
        edit_form = projectform.ProjectForm(user=request.user,
                                            data=request.POST,
                                            files=request.FILES,
                                            instance=project)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('project:project_home')
    context = {
        'project': project,
        'edit_form': edit_form,
        'softskills_divider': softskills_divider,
        'technologies_divider': technologies_divider
    }
    return render(request,
                  'project/edit_project.html',
                  context=context)


@login_required
def delete_project(request, project_id):
    project = get_object_or_404(Project, id=project_id)
    delete_form = projectform.DeleteProjectForm()
    if request.method == 'POST':
        delete_form = projectform.DeleteProjectForm(request.POST)
        if delete_form.is_valid():
            project.delete()
            return redirect('project:project_home')
    context = {
        'project': project,
        'delete_form': delete_form,
    }
    return render(request,
                  'project/delete_project.html',
                  context=context)

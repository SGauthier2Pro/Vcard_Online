from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q

from skill.models.language import Language
from skill.forms import languageform


@login_required
def index(request):
    languages = Language.objects.filter(
        Q(user=request.user)
    )

    return render(request,
                  'skill/languages_index.html',
                  context={'languages': languages}
                  )


@login_required
def create_language(request):
    language_form = languageform.LanguageForm()
    if request.method == 'POST':
        language_form = languageform.LanguageForm(request.POST)
        if language_form.is_valid():
            language_to_save = language_form.save(commit=False)
            language_to_save.user = request.user
            language_to_save.save()
            return redirect('skill:language_home')
    return render(request,
                  'skill/create_language.html',
                  context={'language_form': language_form}
                  )


@login_required
def edit_language(request, language_id):
    language = get_object_or_404(Language,
                                 id=language_id)
    edit_form = languageform.LanguageForm(instance=language)
    if request.method == 'POST':
        edit_form = languageform.LanguageForm(request.POST,
                                              instance=language)
        if edit_form.is_valid():
            edit_form.save()
            return redirect('skill:language_home')
    context = {
        'language': language,
        'edit_form': edit_form,
    }
    return render(request,
                  'skill/edit_language.html',
                  context=context)


@login_required
def delete_language(request, language_id):
    language = get_object_or_404(Language, id=language_id)
    delete_form = languageform.DeleteLanguageForm()
    if request.method == 'POST':
        delete_form = languageform.DeleteLanguageForm(request.POST)
        if delete_form.is_valid():
            language.delete()
            return redirect('skill:language_home')
    context = {
        'language': language,
        'delete_form': delete_form,
    }
    return render(request,
                  'skill/delete_language.html',
                  context=context)

from django import template
import locale

register = template.Library()


@register.filter
def model_type(value):
    return type(value).__name__


@register.filter
def get_posted_at_display(posted_at):
    locale.setlocale(locale.LC_TIME, 'fr_FR')
    return f'{posted_at.strftime("%d/%m/%Y")}'


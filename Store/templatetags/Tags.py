from django import template
from Store.forms import ContactForm

register = template.Library()


@register.filter(name='img')
def img(file):
    if file:
        return file[0].image.url
    else:
        return ""


@register.simple_tag
def length(value, limit):
    if len(value) > limit:
        return value[:limit] + '..'
    else:
        return value


@register.inclusion_tag('ContactForm.html', takes_context=True)
def contact(context):
    context['form'] = ContactForm()
    return context

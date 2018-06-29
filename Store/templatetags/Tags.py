from django import template
from Store.forms import ContactForm, LoginForm

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


@register.inclusion_tag('registration/login.html', takes_context=True)
def login(context):
    context['login_form'] = LoginForm()
    return context


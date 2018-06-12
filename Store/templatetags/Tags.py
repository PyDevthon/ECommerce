from django import template

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

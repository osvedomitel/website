from django import template
from django.template.defaultfilters import stringfilter


WORDS_PER_MINUTE = 180


register = template.Library()


@register.filter
@stringfilter
def reading_time(value):
    minutes = round(len(value.split()) / WORDS_PER_MINUTE)
    return '{} {}'.format(minutes, 'минута' if minutes == 1 else 'минути')

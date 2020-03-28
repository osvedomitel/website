from django import template
from django.template.defaultfilters import stringfilter

from orthography import typography

register = template.Library()


@register.filter
@stringfilter
def add_typography(value):
    return typography.add_typography(value)

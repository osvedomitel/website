from django import template
from django.template.defaultfilters import stringfilter

from orthography import ivanchov


register = template.Library()


@register.filter
@stringfilter
def add_soft_hyphens(value):
    return ivanchov.add_soft_hyphens(value)

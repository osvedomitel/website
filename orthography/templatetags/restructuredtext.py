from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe
from docutils.core import publish_parts


register = template.Library()


@register.filter
@stringfilter
def rest2html(value):
    return mark_safe(publish_parts(value, writer_name='html')['fragment'])

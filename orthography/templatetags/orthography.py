from datetime import date

from django import template
from django.template.defaultfilters import stringfilter

from orthography import ivanchov


MONTH_NAMES = (
    'януарий',
    'февруарий',
    'мартъ',
    'априлъ',
    'май',
    'юний',
    'юлий',
    'августъ',
    'септемврий',
    'октомврий',
    'ноемврий',
    'декемврий',
)


register = template.Library()


@register.filter
@stringfilter
def add_soft_hyphens(value):
    return ivanchov.add_soft_hyphens(value)


@register.filter(expects_localtime=True)
def date_ivanchov(value):
    if value and isinstance(value, date):
        return '{} {} {}'.format(
            value.day, MONTH_NAMES[value.month-1], value.year
        )
    else:
        return ''

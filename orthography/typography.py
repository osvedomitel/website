import re

"""
Filters for some typographic features.

Converts -- to – (n-dash) and --- to — (m-dash).

Converts ASCII double "quotes" to Bulgarian typographic „quotes“.
Converts wrong typographic „quotes” or “quotes” to „quotes“.
"""

LEFT_QUOTE_REGEX = re.compile(
    r"""
    (?:^|(?<=\s))[\"“„”]
    """,
    re.VERBOSE
)

RIGHT_QUOTE_REGEX = re.compile(
    r"""
    [\"“„”](?:$|(?=[\s,:;\.!\?]))
    """,
    re.VERBOSE
)

LEFT_QUOTE = '„'
RIGHT_QUOTE = '“'

def convert_dashes(text):
    return text.replace('---', '—').replace('--', '–')

def convert_quotes(text):
    return RIGHT_QUOTE_REGEX.sub(RIGHT_QUOTE, LEFT_QUOTE_REGEX.sub(LEFT_QUOTE, text))

def add_typography(text):
    return convert_quotes(convert_dashes(text))

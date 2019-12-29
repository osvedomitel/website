import re


SOFT_HYPHEN = '­'


MATCH_SYLLABLES_REGEX = re.compile(
    r"""
    (
        [бвгджзйклмнпрстфхцчшщ]*
        (?:[аеиоуъѣюѫя]|ьо)
        (?:й(?![аеиоуъѣюѫя]))?
        (?:[бвгджзйклмнпрстфхцчшщ]+[ъь]?(?=$))?
        (?:[бвгджзйклмнпрстфхцчшщ](?=[бвгджзйклмнпрстфхцчшщ]+[аеиоуъьѣюѫя]))?
    )
    """,
    flags=re.IGNORECASE | re.VERBOSE
)


MATCH_WORDS_REGEX = re.compile(
    r"([абвгдежзийклмнопрстуфхцчшщъьѣюѫя]+)",
    flags=re.IGNORECASE
)


def syllabify(word, hyphen=SOFT_HYPHEN):
    return hyphen.join(filter(None, MATCH_SYLLABLES_REGEX.split(word)))


def add_soft_hyphens(text):
    def replace(match):
        return syllabify(match.group(0))
    return MATCH_WORDS_REGEX.sub(replace, text)

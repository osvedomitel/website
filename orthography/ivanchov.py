import re


SOFT_HYPHEN = '­'


MATCH_SYLLABLES_REGEX = re.compile(
    r"""
    (
        [бвгджзйклмнпрстфцчшщ]*
        (?:[аеиоуъѣюѫя]|ьо)
        (?:й(?![аеиоуъѣюѫя]))?
        (?:[бвгджзйклмнпрстфцчшщ]+[ъь]?(?=$))?
        (?:[бвгджзйклмнпрстфцчшщ](?=[бвгджзйклмнпрстфцчшщ]+[аеиоуъьѣюѫя]))?
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

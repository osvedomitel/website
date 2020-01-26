import re


SOFT_HYPHEN = '­'

# the stress mark is a combining grave accent
STRESS_MARK = "\u0300"

# all consonants proper
CONSONANT = "[бвгджзйклмнпрстфхцчшщ]"

# all vowels proper
# (Ь is included as a full vowel even though it's a bit special but it doesn't hurt)
# vowels can be preceded by an optional Ь or followed by an optional stress mark
# only И and Е have dedicated unicode codepoints for the stressed versions
VOWEL = "(?:ь?[аъоуеѐиѝьюяѣѫѭ]" + STRESS_MARK + "?)"

# all letters
LETTER = "(?:" + CONSONANT + "|" + VOWEL + ")"

MATCH_SYLLABLES_REGEX = re.compile(
    rf"""
    (
        # zero or more consonants
        {CONSONANT}*
        # a vowel
        (?:{VOWEL})
        # optional Й (not followed by a vowel except for И)
        (?:й(?:(?!{VOWEL})|(?=[иѝ])))?
        # optional: one or more consonants and an optional Ъ/Ь (at the end of the word)
        (?:{CONSONANT}+[ъь]?(?=$))?
        # optional: a consonant (followed by other consonant(s) + vowel)
        (?:{CONSONANT}(?={CONSONANT}+{VOWEL}))?
        # optional: a consonant + ь (followed by та at the end of the word), e.g. про-лѣть-та
        (?:{CONSONANT}+ь(?=та{STRESS_MARK}?$))?
    )
    """,
    flags=re.IGNORECASE | re.VERBOSE
)

MATCH_WORDS_REGEX = re.compile(
    rf"({LETTER}+)",
    flags=re.IGNORECASE
)

ILLEGAL_SYLLABLE_REGEX = re.compile(
    rf"^(?:{VOWEL}|тъ)$",
    flags=re.IGNORECASE
)

def join_illegal_syllables(syllables):
    syllables = list(syllables)
    if ILLEGAL_SYLLABLE_REGEX.match(syllables[0]):
        syllables[:2] = [''.join(syllables[:2])]
    if ILLEGAL_SYLLABLE_REGEX.match(syllables[-1]):
        syllables[-2:] = [''.join(syllables[-2:])]
    return syllables

def syllabify(word, hyphen=SOFT_HYPHEN):
    return hyphen.join(join_illegal_syllables(filter(None, MATCH_SYLLABLES_REGEX.split(word))))


def add_soft_hyphens(text):
    def replace(match):
        return syllabify(match.group(0))
    return MATCH_WORDS_REGEX.sub(replace, text)

import unittest

from orthography.typography import convert_dashes, convert_quotes


class DashesTestCase(unittest.TestCase):

    def ok(self, ascii_dashes, fancy_dashes):
        self.assertEqual(convert_dashes(ascii_dashes), fancy_dashes)

    def test_basic(self):
        self.ok('проба--или не', 'проба–или не')
        self.ok('наболѣлъ проблемъ подъ тепетата -- градътъ се кичи съ златенъ медалъ',
                'наболѣлъ проблемъ подъ тепетата – градътъ се кичи съ златенъ медалъ')
        self.ok('най-новото---и още по-дълго тире', 'най-новото—и още по-дълго тире')

class QuotesTestCase(unittest.TestCase):

    def ok(self, bad_quotes, good_quotes):
        self.assertEqual(convert_quotes(bad_quotes), good_quotes)

    def test_basic(self):
        self.ok('язовиръ "Студена", и разрухата', 'язовиръ „Студена“, и разрухата')
        self.ok('язовиръ “Студена”, и разрухата', 'язовиръ „Студена“, и разрухата')
        self.ok('язовиръ „Студена”, и разрухата', 'язовиръ „Студена“, и разрухата')
        self.ok('празни "" въ срѣдата', 'празни „“ въ срѣдата')
        self.ok('"Началото" и "сѫщото". "Другото", "третото"; "петото".',
                '„Началото“ и „сѫщото“. „Другото“, „третото“; „петото“.')
        self.ok('"това"?\n"онова"!', '„това“?\n„онова“!')
        self.ok('"това":\n"онова";', '„това“:\n„онова“;')
        self.ok('той (язовиръ "Студена") е празенъ', 'той (язовиръ „Студена“) е празенъ')
        self.ok('("Студена")', '(„Студена“)')
        self.ok('той [язовиръ "Студена"] е празенъ', 'той [язовиръ „Студена“] е празенъ')
        self.ok('["Студена"]', '[„Студена“]')
        self.ok('""', '„“')


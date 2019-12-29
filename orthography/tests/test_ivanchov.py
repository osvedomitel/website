import unittest

from orthography.ivanchov import syllabify


class SyllabifyTestCase(unittest.TestCase):

    def ok(self, without_hyphens, with_hyphens):
        self.assertEqual(syllabify(without_hyphens, '-'), with_hyphens)

    def test_basic(self):
        self.ok('издателство', 'из-да-тел-ство')
        self.ok('конь', 'конь')
        self.ok('линеенъ', 'ли-не-енъ')
        self.ok('постоянство', 'пос-то-ян-ство')
        self.ok('пролетта', 'про-лет-та')
        self.ok('радостъ', 'ра-достъ')
        self.ok('странникъ', 'стран-никъ')
        self.ok('хронология', 'хро-но-ло-ги-я')

    def test_y(self):
        self.ok('достойнство', 'дос-тойн-ство')
        self.ok('Йорданъ', 'Йор-данъ')
        self.ok('който', 'кой-то')
        self.ok('покой', 'по-кой')
        self.ok('районъ', 'ра-йонъ')
        self.ok('случайность', 'слу-чай-ность')

    def test_er(self):
        self.ok('Кольо', 'Ко-льо')
        self.ok('фотьойлъ', 'фо-тьойлъ')
        self.ok('шофьоръ', 'шо-фьоръ')

    def test_yat(self):
        self.ok('бѣлитѣ', 'бѣ-ли-тѣ')
        self.ok('освѣдомитель', 'ос-вѣ-до-ми-тель')
        self.ok('прѣзъ', 'прѣзъ')

    def test_yus(self):
        self.ok('бѫдѫ', 'бѫ-дѫ')
        self.ok('пѫнъ', 'пѫнъ')
        self.ok('ѫгълъ', 'ѫ-гълъ')

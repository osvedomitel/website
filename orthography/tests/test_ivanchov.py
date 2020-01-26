import unittest

from orthography.ivanchov import syllabify, add_soft_hyphens, SOFT_HYPHEN


class SyllabifyTestCase(unittest.TestCase):

    def ok(self, without_hyphens, with_hyphens):
        self.assertEqual(syllabify(without_hyphens, '-'), with_hyphens)

    def test_basic(self):
        self.ok('издателство', 'из-да-тел-ство')
        self.ok('изда̀телство', 'из-да̀-тел-ство')
        self.ok('конь', 'конь')
        self.ok('ко̀нь', 'ко̀нь')
        self.ok('езикъ', 'езикъ')
        self.ok('езѝкъ', 'езѝкъ')
        self.ok('линеенъ', 'ли-не-енъ')
        self.ok('линѐенъ', 'ли-нѐ-енъ')
        self.ok('постоянство', 'пос-то-ян-ство')
        self.ok('постоя̀нство', 'пос-то-я̀н-ство')
        self.ok('пролѣтьта', 'про-лѣть-та')
        self.ok('пролѣтьта̀', 'про-лѣть-та̀')
        self.ok('радость', 'ра-дость')
        self.ok('ра̀дость', 'ра̀-дость')
        self.ok('странникъ', 'стран-никъ')
        self.ok('стра̀нникъ', 'стра̀н-никъ')
        self.ok('хронология', 'хро-но-ло-гия')
        self.ok('хроноло̀гия', 'хро-но-ло̀-гия')

    def test_y(self):
        self.ok('достойнство', 'дос-тойн-ство')
        self.ok('досто̀йнство', 'дос-то̀йн-ство')
        self.ok('Йорданъ', 'Йор-данъ')
        self.ok('Йорда̀нъ', 'Йор-да̀нъ')
        self.ok('който', 'кой-то')
        self.ok('ко̀йто', 'ко̀й-то')
        self.ok('покой', 'по-кой')
        self.ok('поко̀й', 'по-ко̀й')
        self.ok('районъ', 'ра-йонъ')
        self.ok('райо̀нъ', 'ра-йо̀нъ')
        self.ok('случайность', 'слу-чай-ность')
        self.ok('случа̀йность', 'слу-ча̀й-ность')

    def test_er(self):
        self.ok('Кольо', 'Ко-льо')
        self.ok('Ко̀льо', 'Ко̀-льо')
        self.ok('фотьойлъ', 'фо-тьойлъ')
        self.ok('фотьо̀йлъ', 'фо-тьо̀йлъ')
        self.ok('шофьоръ', 'шо-фьоръ')
        self.ok('шофьо̀ръ', 'шо-фьо̀ръ')
        self.ok('учительтъ', 'учи-те-льтъ')
        self.ok('учѝтельтъ', 'учѝ-те-льтъ')

    def test_er_fem(self):
        self.ok('кръвьта', 'кръвь-та')
        self.ok('кръвьта̀', 'кръвь-та̀')
        self.ok('любовьта', 'лю-бовь-та')
        self.ok('любовьта̀', 'лю-бовь-та̀')
        self.ok('костьта', 'кость-та')
        self.ok('костьта̀', 'кость-та̀')
        self.ok('потьта', 'поть-та')
        self.ok('потьта̀', 'поть-та̀')

    def test_yat(self):
        self.ok('бѣлитѣ', 'бѣ-ли-тѣ')
        self.ok('бѣ̀литѣ', 'бѣ̀-ли-тѣ')
        self.ok('освѣдомитель', 'ос-вѣ-до-ми-тель')
        self.ok('освѣдомѝтель', 'ос-вѣ-до-мѝ-тель')
        self.ok('прѣзъ', 'прѣзъ')
        self.ok('прѣ̀зъ', 'прѣ̀зъ')

    def test_yus(self):
        self.ok('бѫдѫ', 'бѫ-дѫ')
        self.ok('бѫ̀дѫ', 'бѫ̀-дѫ')
        self.ok('пѫнъ', 'пѫнъ')
        self.ok('пѫ̀нъ', 'пѫ̀нъ')
        self.ok('ѫгълъ', 'ѫгълъ')
        self.ok('ѫ̀гълъ', 'ѫ̀гълъ')
        self.ok('ѫгловатъ', 'ѫг-ло-ватъ')
        self.ok('ѫглова̀тъ', 'ѫг-ло-ва̀тъ')

    def test_iyus(self):
        self.ok('неѭ', 'неѭ')
        self.ok('нѐѭ', 'нѐѭ')
        self.ok('стоѭ', 'стоѭ')
        self.ok('стоѭ̀', 'стоѭ̀')
        self.ok('постоѭ', 'пос-тоѭ')
        self.ok('постоѭ̀', 'пос-тоѭ̀')
        self.ok('паѭкъ', 'па-ѭкъ')
        self.ok('па̀ѭкъ', 'па̀-ѭкъ')
        self.ok('говорѭтъ', 'го-во-рѭтъ')
        self.ok('гово̀рѭтъ', 'го-во̀-рѭтъ')

    def test_monstrosity(self):
        self.ok("стройиндустрийностьта", "строй-ин-дус-трий-ность-та")
        self.ok("стро̀йѝнду̀стрѝйно̀стьта̀", "стро̀й-ѝн-ду̀с-трѝй-но̀сть-та̀")
        self.ok("гьонсуратшофьорлия", "гьон-су-рат-шо-фьор-лия")
        self.ok("гьо̀нсу̀ра̀тшо̀фьо̀рлѝя̀", "гьо̀н-су̀-ра̀т-шо̀-фьо̀р-лѝя̀")

class AddSoftHyphensTestCase(unittest.TestCase):

    def ok(self, without_hyphens, with_hyphens):
        self.assertEqual(add_soft_hyphens(without_hyphens), with_hyphens.replace('-', SOFT_HYPHEN))

    def test_basic(self):
        self.ok('новото издателство на Освѣдомитель', 'но-во-то из-да-тел-ство на Ос-вѣ-до-ми-тель')

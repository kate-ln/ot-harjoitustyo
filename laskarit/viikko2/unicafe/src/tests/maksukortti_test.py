import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_konstruktori_asettaa_saldon_oikein(self):
        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahan_lataaminen_kasvattaa_saldoa_oikein(self):
        self.maksukortti.lataa_rahaa(2500)

        self.assertEqual(self.maksukortti.saldo_euroina(), 35.00)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 35.00 euroa")

    def test_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(1000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 0.00)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 0.00 euroa")

    def test_saldo_ei_muutu_jos_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(2000)

        self.assertEqual(self.maksukortti.saldo_euroina(), 10.00)
        self.assertEqual(str(self.maksukortti), "Kortilla on rahaa 10.00 euroa")

    def test_rahat_riittavat(self):
        kortti = Maksukortti(250)
        self.assertEqual(kortti.ota_rahaa(250), True)

    def test_rahat_eivat_riita(self):
        kortti = Maksukortti(250)
        self.assertEqual(kortti.ota_rahaa(300), False)
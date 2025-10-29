import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassa = Kassapaate()
        self.kortti = Maksukortti(1000)

    def test_kassapaatteen_rahamaara_oikea(self):
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)

    def test_myytyjen_lounaiden_maara_oikea(self):
        self.assertEqual(self.kassa.edulliset + self.kassa.maukkaat, 0)

    def test_maksu_riittava_kassa_edulliset(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(500), 260)
        self.assertEqual(self.kassa.kassassa_rahaa, 100240)
        self.assertEqual(self.kassa.edulliset, 1)
    
    def test_maksu_riittava_kassa_maukkaat(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(500), 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100400)
        self.assertEqual(self.kassa.maukkaat, 1)

    def test_maksu_ei_riittava_kassa_edulliset(self):
        self.assertEqual(self.kassa.syo_edullisesti_kateisella(100), 100)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.edulliset, 0)
    
    def test_maksu_ei_riittava_kassa_maukkaat(self):
        self.assertEqual(self.kassa.syo_maukkaasti_kateisella(300), 300)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        self.assertEqual(self.kassa.maukkaat, 0)
    
    def test_kortilla_on_tarpeeksi_rahaa_edulliset(self):
        self.assertEqual(self.kortti.ota_rahaa(250), True)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(self.kortti), True)
        self.assertEqual(self.kassa.edulliset, 1)
        
    def test_kortilla_on_tarpeeksi_rahaa_maukkaat(self):
        self.assertEqual(self.kortti.ota_rahaa(400), True)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(self.kortti), True)
        self.assertEqual(self.kassa.maukkaat, 1)
    
    def test_kortilla_ei_tarpeeksi_rahaa_edulliset(self):
        kortti = Maksukortti(100)
        self.assertEqual(kortti.ota_rahaa(250), False)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassa.syo_edullisesti_kortilla(kortti), False)
        self.assertEqual(self.kassa.edulliset, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
        
    def test_kortilla_ei_tarpeeksi_rahaa_maukkaat(self):
        kortti = Maksukortti(100)
        self.assertEqual(kortti.ota_rahaa(400), False)
        self.assertEqual(kortti.saldo, 100)
        self.assertEqual(self.kassa.syo_maukkaasti_kortilla(kortti), False)
        self.assertEqual(self.kassa.maukkaat, 0)
        self.assertEqual(self.kassa.kassassa_rahaa, 100000)
    
    def test_kortille_ladataan_rahaa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, 1000)
        self.assertEqual(self.kortti.saldo, 2000)
        self.assertEqual(self.kassa.kassassa_rahaa, 101000)

    def test_kortille_ladataan_negatiivinen_summa(self):
        self.kassa.lataa_rahaa_kortille(self.kortti, -1000)
    
    def test_kassassa_rahaa_euroina(self):
        self.assertEqual(self.kassa.kassassa_rahaa_euroina(), 1000.00)

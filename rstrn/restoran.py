class Restoran():
    Restoran_nim = ""
    Soogi_tyyp = ""

    def kirj_resto(self):
        kirj_tekst = self.restorani_nimi, "pakub", self.soogi_tyyp
        print(kirj_tekst)
    def ava_restoraan(self):
        print(self.restorani_nimi, "on avatud")
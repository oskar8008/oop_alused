class Kasutajad():
    eesnim = ""
    perenim = ""
    email = ""
    vanus = 0

    def kirjelda_kasutaja(self):
        print("kasutaja ees- j aprerkonna nimi on:  {0} {1} ".__format__(self.eesnim,self.perenim))
        print("kasutaja email onm : {0} ".format(self.email) )

    def tervita_kasutajat(self):
        print("tere, {0} {1}" .format(self.eesnim , self.perenim))



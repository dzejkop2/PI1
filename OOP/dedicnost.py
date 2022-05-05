#dedičnosť
class Zvieratko:
    def __init__(self,meno):
        self.meno = meno
    def jedz(self,jedlo):
        print(f"{self.meno}: {jedlo} mi chutná!")

class Macka(Zvieratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Haf")
    def jedz(self,jedlo):
        super().jedz("šunka")
        print(f"{self.meno}: {jedlo} mi nechutná!")

class Pes(Zvieratko):
    def urob_zvuk(self):
        print(f"{self.meno}: Haf")

macka = Macka("Micka")
pes = Pes("Falko")

macka.jedz("šunka")
macka.zamnaukaj()

pes.jedz("Granula")

#polymorfismus
zvieratka = [Macka("Naginy"), Pes("Azor")]

for zvieratko in zvieratka:
    zvieratko.jedz("granula")
    zvieratko.urob_zvuk()

#generalizacia

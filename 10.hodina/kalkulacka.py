class Calculator:
    def __init__(self,cislo1,cislo2):
        self.cislo1 = cislo1
        self.cislo2 = cislo2
    def sucet(self):
        vysledok = self.cislo1 + self.cislo2
        return vysledok
    def rozdiel(self):
        vysledok = self.cislo1 - self.cislo2
        return vysledok
    def nasobenie(self):
        vysledok = self.cislo1 * self.cislo2
        return vysledok
    def delenie(self):
        vysledok = self.cislo1 / self.cislo2
        return vysledok

def matika():
    cislo1 = int(input("Zadaj 1. cislo: "))
    cislo2 = int(input("Zadaj 2. cislo: "))
    kalkulacka = Calculator(cislo1,cislo2)
    print(f"Sucet: {str(kalkulacka.sucet())}")
    print(f"Rozdiel: {str(kalkulacka.rozdiel())}")
    print(f"Nasobenie: {str(kalkulacka.nasobenie())}")
    print(f"Delenie: {str(kalkulacka.delenie())}")



matika()
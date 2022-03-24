class Auto:
    def __init__(self,znacka,rokVyroby,farba,pocetMiest,jeNastartovane):
        self.znacka = znacka
        self.rokVyroby = rokVyroby
        self.farba = farba
        self.pocetMiest = pocetMiest
        self.jeNastartovane = jeNastartovane

    def __str__(self):
        print("Značka auta je: " + self.znacka)
        print("Rok výroby auta je: " + str(self.rokVyroby))
        print("Farba auta je: " + self.farba)
        print("Auto má " + str(self.pocetMiest) + " miest")
        print("Auto je naštartované: " + str(self.jeNastartovane))
        return ""
    def chod_dopredu(self):
        print("Auto ide dopredu")
    def zatrub(self):
        print("tuuuuuuuuuuuuuuuuuuuuuut")
    def zapniMotor(self, state):
        self.jeNastartovane = state

auto = Auto("BMW", 1999, "Biela", 5, "jj")
print(auto)
class Cat:
    # KONŠTRUKTOR
    def __init__(self, name, vek):
        print("vytvaram objekt mačky")
        self.name = name
        self.vek = vek

    def __str__(self):
        print("Meno mačky je: " + self.name)
        print("Vek mačky je:" + str(self.vek))
        return  "";
    def zamnaukaj(self):
        print(self.name + " mňau")

    def zjedz(self, jedlo):
        print(self.name + " zjedla/zjedlo " + jedlo)

# INŠTANICA OBJEKTU
cat = Cat("Mica", 4)
#cat.meno = "Cica"
#volanie metody
cat.zamnaukaj()
cat.zjedz("rybu")

cat2 = Cat("Murko", 5)
#cat2.meno = "Murko"
cat2.zamnaukaj()
print(cat2)
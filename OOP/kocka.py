import random
class Kocka:
    def __init__(self,strany,hody):
        self.strany = strany
        self.hody = hody

    def hod_kocky(self):
        for i in range(self.hody):
            hod = random.randint(1,self.strany)
            print(str(hod) + " ", end='')

pocetStran = int(input("Zadaj pocet stran kocky: "))
pocetHodov = int(input("Zadaj pocet hodov: "))
kocka = Kocka(pocetStran,pocetHodov)
kocka.hod_kocky()
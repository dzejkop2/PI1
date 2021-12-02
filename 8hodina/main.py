import random

mena = []
privlastky = ["maly", "velky", "pekny", "skaredy", "chudy", "tucny", "vesely", "smutny", "nudny", "zaujimavy"]

while True:
    meno = input("Zadaj meno: ")
    if meno == "koniec":
        break
    priezvisko = input("Zadaj meno: ")

    mismas = meno + " " + privlastky[random.randint(0,9)] + " " + priezvisko
    mena.append(mismas)

    for i in range(1, len(mena) + 1):
        print(str(i) + ".\t" + mena[i - 1])
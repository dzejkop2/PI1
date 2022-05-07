print("Zadávaj čísla a potom stlač ENTER")
opakovanie = 1
zoznamcisel = []
while opakovanie != "":
    zadanecislo = input("Zadaj čislo: ")
    opakovanie = zadanecislo
    if zadanecislo == "":
        break
    vstup = int(zadanecislo)
    zoznamcisel.append(zadanecislo)


dlzkazoznamu = len(zoznamcisel)
mediancislo = int(dlzkazoznamu / 2)
median = int(zoznamcisel[mediancislo])
for i in range(dlzkazoznamu):
    cislo = zoznamcisel[i]
    cislo = int(cislo)
    rozdielcisla = cislo - median
    print(cislo,"sa od medianu líši o", rozdielcisla)

print(median)
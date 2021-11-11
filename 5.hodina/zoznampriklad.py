cisla = list(range(10,0,-1))
for i in cisla:
    print(i)

print(cisla)

opakovanie = "ano"
ovocie = ["jablko","banan","hruska","malina"]
zelenina = ["zemiak","cibula","uhorka","brokolica","paradajka"]

while opakovanie == "ano":
    jedlo = input("Zadaj ovocie alebo zeleninu: ")

    if jedlo in ovocie:
        print("Zadal si ovocie")
    elif jedlo in zelenina:
        print("Zadal si zeleninu")
    else:
        print("Toto slovo neni v mojom zozname")

    opakovanie = input("Chceš zadať ďalšie jedlo? ")
    if opakovanie == "nie":
        opakovanie = "nie"

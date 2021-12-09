hracia_plocha = [
    [" ",1,2,3],
    [1," "," "," "],
    [2," "," "," "],
    [3," "," "," "]
    ]

def vypisPlochy(hracia_plocha):
    for riadok in hracia_plocha:
        for policko in riadok:
            print(policko, end="")
        print()

while True:
    vypisPlochy(hracia_plocha)
    print("Na rade je hrac s krizikmi")
    poloha1 = int(input("Zadaj polohu 1: "))
    if poloha1 > 3:
        print("Zadaj mensie cislo")
    elif poloha1 == 0:
        print("Zadaj vacsie cislo")

    poloha2 = int(input("Zadaj polohu 2: "))
    if poloha2 > 3:
        print("Zadaj mensie cislo")
    elif poloha2 == 0:
        print("Zadaj vacsie cislo")
    vkladanie = hracia_plocha[poloha1][poloha2] = "X"

    vypisPlochy(hracia_plocha)
    print("Na rade je hrac s kruzkami")
    poloha1 = int(input("Zadaj polohu 1: "))
    if poloha1 > 3:
        print("Zadaj mensie cislo")
    elif poloha1 == 0:
        print("Zadaj vacsie cislo")
    poloha2 = int(input("Zadaj polohu 2: "))
    if poloha2 > 3:
        print("Zadaj mensie cislo")
    elif poloha2 == 0:
        print("Zadaj vacsie cislo")
    vkladanie = hracia_plocha[poloha1][poloha2] = "O"


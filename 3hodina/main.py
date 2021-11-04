"""
start = int(input("Zadaj pociatocne cislo: "))
koniec  = int(input("Zadaj koncove cislo: "))

while (start <= koniec):
    if (start % 3 == 0):
        print(start)
    start = start + 1
"""
"""
samohlasky = "aáeéiíouúyý"
spoluhlasky = "qwrtopsdfghjklxcvbnm"
cislo = "1234567890"

slovo = input("Zadaj slovo")

pocet_samohlasok = 0
pocet_spoluhlasok = 0
pocet_cisel = 0
pocet_znakov = 0


for znak in slovo:
    if znak in samohlasky:
        pocet_samohlasok = pocet_samohlasok + 1
    elif znak in spoluhlasky:
        pocet_spoluhlasok = pocet_spoluhlasok + 1
    elif znak in cislo:
        pocet_cisel = pocet_cisel + 1
    else:
        pocet_znakov = pocet_znakov + 1

print("Slovo obsahuje:")
print(pocet_spoluhlasok, "spoluhlasok")
print(pocet_samohlasok, "samohlasok")
print(pocet_cisel, "cisel")
print(pocet_znakov, "znakov")
"""
"""
riadky = int(input("Zadaj počet riadkov:"))
stlpce = int(input("Zadaj počet stlpcov:"))

for i in range(0,stlpce):
    for j in range(0,riadky):
        print("*", end="")
    print()
"""
#vyska = int(input("Zadaj vysku trojuholnika"))



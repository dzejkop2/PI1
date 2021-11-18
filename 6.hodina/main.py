from random import randrange, uniform

domy = []

for y in range(15):
    x = randrange(0, 10)
    domy.append(x)

spoluObyvatelov = sum(domy)
neobyvaneDomy = 0
pocetObyvatelov = 0
maximalnyPocetObyvatelov = max(domy)
maximalneDomy = 0

for i in domy:
    if i == 0:
        neobyvaneDomy += 1
    if i == maximalnyPocetObyvatelov:
        maximalneDomy += 1

print("Neobyvanych domov je", neobyvaneDomy)
print("Pocet obyvateľov je", spoluObyvatelov)
print("Maximálny počet obyvateľov v dome je", maximalnyPocetObyvatelov)
print("Počet maximalnych domov je", maximalneDomy)

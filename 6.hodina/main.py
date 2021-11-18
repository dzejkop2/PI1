domy = [1, 2, 3, 4, 5, 0, 0, 4, 5]

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
print("Maximalny počet obyvateľov v dome je", maximalnyPocetObyvatelov)
print("Počet maximalnych domov je", maximalneDomy)
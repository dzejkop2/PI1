"""
pole = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

print(pole[1][1])
pole[0].append(99);
print("-----------")
for riadok in pole:
    for prvok in riadok:
        print(prvok)
print("-----------")
"""
def vypisKinosalu(kinosala):
    for riadok in kinosala:
        print(riadok)

kinosala = []

for i in range(5):
    temp = []
    for i in range(10):
        temp.append(0)
    kinosala.append(temp)

vypisKinosalu(kinosala)
print()
kinosala[0][5] = 1
kinosala[2][4] = 1
kinosala[1][3] = 1
vypisKinosalu(kinosala)
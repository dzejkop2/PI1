slova = []
a = -1
subory = int(input("Zadaj koľko súborov chceš vytvoriť: "))

slovo_subor = [a + 1]



with open("./basnicka.txt", encoding="utf-8") as subor:
    for riadok in subor:
        slova += riadok.split()

for i in range(subory):
    open("%s.txt" % i, "w").write(slova[i])
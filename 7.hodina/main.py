input = 

with open("./basnicka.txt", encoding="utf-8") as subor:
    for riadok in subor:
        input += riadok.split()

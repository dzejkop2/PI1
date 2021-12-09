bielyRiadok = ["█", " ", "█", " ", "█", " ", "█", " "]
ciernyRiadok = [" ", "█", " ", "█", " ", "█", " ", "█"]

for i in range(4):
    for pismeno in ciernyRiadok:
        print(pismeno, end= "")
    print(sep= "")
    for pismeno in bielyRiadok:
        print(pismeno, end="")
    print("")
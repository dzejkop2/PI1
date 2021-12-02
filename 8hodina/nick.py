import random

skupina1 = []
skupina2 = []
skupina3 = []

while True:
    nick = input("Zadaj meno: ")
    if nick == "":
        break
    skupina = random.randint(0,2)
    if skupina == 0:
        skupina1.append(nick)
    elif skupina == 1:
        skupina2.append(nick)
    elif skupina == 2:
        skupina3.append(nick)
    print("V 2.skupine su: ", skupina2)
    print("V 3.skupine su: ", skupina3)
    print("V 1.skupine su: ", skupina1)
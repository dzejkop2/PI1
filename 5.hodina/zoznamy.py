
zoznam_prazdny = []
zoznam_cisel = [1,5,8,9,15]
zoznam_pismen = ["a","t","r"]
zoznam_mix = ["slovo", 14, "a", "@", 55]



zoznam = list()
print(zoznam)
zoznam_range = list(range(3, 7))
print(zoznam_range)

print("--------")

neorezany_zoznam = list(range(10))
print(neorezany_zoznam)

print(neorezany_zoznam[0:5])
print(neorezany_zoznam[2:8])
print(neorezany_zoznam[1:6])

#velkosť zoznamu
x = [5, 8, 1, 3,"slovo"]
print(len(x))

#prechádzanie zoznamu
zoznam_prvkov = ["jablko", "hruška", "banan"]

#1
for prvok in zoznam_prvkov:
    print(prvok)

for index in range(len(zoznam_prvkov)):
    print(zoznam_prvkov[index])

#metody pre zoznamy
myList = [1,5,8,55,500]
#append -> prida nakoniec prvok

myList.append(99)
myList.append(1)
print(myList)

#pop
myList = myList.pop()
print(myList)

#funkcie
#min/max
myList2 = [1,2,5,10,74,-10]
print("minimum",min(myList2))
print("maximum",max(myList2))
print("suma",sum(myList2))

print(sorted(myList2))
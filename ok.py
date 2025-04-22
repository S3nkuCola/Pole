#1
pole = ["kniha", "tužka", "propiska", "penál", "tabule", "sešit"]
#2
print("Délka pole: ", len(pole))
for prvek in pole:
    print(prvek)
#3
prvekDva = input("Zadejte nový prvek: ")
pole.append(prvekDva)
#4
odstranit = pole.pop(4)
print("Odstraněný prvek: ", odstranit)
#5
pole.sort()
print("Seřazené pole:", pole)
#6
pole.reverse()
print("Obrácené pole:", pole)
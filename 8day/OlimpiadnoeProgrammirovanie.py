#Zadacha 1.1
def f(n):
    if n[0] >= n[1]:
        return  f(n[1:])
    if n[1] >= n[2] and n[2] >= n[3]:
        del n[1]
        return  f(n)

    return n

print(f([6, 2, 5, 4, 2, 5, 6]))




#Zadacha 1.2
dano = [6, 2, 5, 4, 2, 5, 6]

#длина наибольшей последовательности
karetka = [1] * len(dano) #заполняю единицами на длину изнач. последовательности
for tek_el in range(len(dano)):
    for sled_el in range(tek_el): #перебираю все элементы перед текущим
        if dano[sled_el] < dano[tek_el]: #если выполняется условие
            #выбираю мах из между уже найденной и возможной длинной sled_el + 1
            karetka[tek_el] = max(karetka[tek_el], karetka[sled_el] + 1)

print(f"макс длина: {max(karetka)}")
print(f"удалено: {len(dano) - max(karetka)}\n")












































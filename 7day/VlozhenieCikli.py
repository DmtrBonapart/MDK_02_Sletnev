#Zadacha 1
for x in range(15): #перебераю Х от 0 до 14
    #сумма в десятичной
    summa = int(f"123{x}5", 15) + int(f"1{x}233", 15)

    #деление на 14
    if summa % 14 == 0:
        itog10 = summa // 14

        #перевожу в 15
        cifri = "0123456789ABCDE"
        itog15 = "" #сюда сохраню

        perevodimoe_chislo = itog10
        while perevodimoe_chislo > 0:
            itog15 = cifri[perevodimoe_chislo % 15] + itog15 #добавляю цифру в начало строки
            perevodimoe_chislo = perevodimoe_chislo // 15 #продолжаю работать пока не станет 0


        print(f"Z-1: ответ в 10 = {itog10}, ответ в 15 = {itog15}\n")
        break




#Zadacha 2
chislo1 = "AB267D1"
chislo2 = "F024A89"


#так как максимальное F, то до F
vse_cifri = "0123456789ABCDEF"

summa1 = 0
for simvol in chislo1:
    #определяю значение символа
    for i in range(len(vse_cifri)):
        if vse_cifri[i] == simvol:
            summa1 += i
            break

summa2 = 0
for simvol in chislo2:
    for i in range(len(vse_cifri)):
        if vse_cifri[i] == simvol:
            summa2 += i
            break

summa_cifr = summa1 + summa2 #98

print("Z-2 Ответ:")
print(f"cумма цифр 2-х чисел: {summa_cifr}")

#так-как F(15) - макс цифра, то p > 15
for p in range(16, summa_cifr+1): #нахожу минимальный следующий делитель
    if summa_cifr % (p - 1) == 0:
        #первое число в 10
        chislo1_10 = 0
        for simvol in chislo1:
            for i in range(len(vse_cifri)):
                if vse_cifri[i] == simvol:
                    chislo1_10 = chislo1_10 * p + i
                    break

        #второе число в 10
        chislo2_10 = 0
        for simvol in chislo2:
            for i in range(len(vse_cifri)):
                if vse_cifri[i] == simvol:
                    chislo2_10 = chislo2_10 * p + i
                    break

        summa_chisel = chislo1_10 + chislo2_10

        #проверяю делимость
        if summa_chisel % (p - 1) == 0:
            print(f"число_1 в {p}: {chislo1_10}")
            print(f"число_2 в {p}: {chislo2_10}")
            print(f"делится на {p - 1}: {summa_chisel} / {p - 1} = {summa_chisel // (p - 1)}\n")
        break



#Zadacha 3
#xB09 в 17
#x8E8 в 15
#перебираем X в десятичной
for x in range(10):
    chislo1 = x * (17 ** 3) + 11 * (17 ** 2) + 0 * 17 + 9

    chislo2 = x * (15 ** 3) + 8 * (15 ** 2) + 14 * 15 + 8

    summa = chislo1 + chislo2

    #проверяем делимость на 155
    if summa % 155 == 0:
        chastnoe = summa // 155
        print(f"x = {x}")
        print(f"chislo1: {chislo1}")
        print(f"chislo2: {chislo2}")
        print(f"сумма: {summa}")
        print(f"частное в 10: {chastnoe}\n")
        break



#Zadacha 4
sistema = '0123456789AB'
for x1 in range(8): #перебираю все X в 8
    for y1 in range(1, 8): #перебираю все Y от 1 до 7 без 0, т.к. Y в начале числа
        x = sistema[x1] #получаю символы
        y = sistema[y1]
        chislo_1 = int(y + '04' + x + '5', 11) #перевожу из 11 в 10
        chislo_2 = int('253' + x + y, 8) #перевожу из 8 в 10
        sum = chislo_1 + chislo_2

        if sum % 117 == 0:
            print("Z-4:")
            print(f"x={x}, y={y}")
            print(f"ответ: {sum // 117}\n")



#Zadacha 5
dano = (7 * (512 ** 1912)
        + 6 * (64 ** 1954)
        - 5 * (8 ** 1991)
        - 4 * (8 ** 1980)
        - 2022)
itog = "" #хранилище
while dano > 0:
    x = str(dano % 8)
    itog = itog + x
    dano = dano // 8

schetckik = 0
for i in itog:
    if i == "7":
        schetckik += 1
print(f"Z-3: {schetckik}")

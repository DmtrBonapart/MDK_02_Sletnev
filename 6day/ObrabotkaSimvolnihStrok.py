#Zadacha 1
with open('27686.txt', 'r') as moi_file:
    stroka = moi_file.read()

itog_dlinna = 0
tekuschaya_dlinna = 0

for simvol in stroka: #прохожу по каждому символу
    if simvol == 'X': #при условии
        tekuschaya_dlinna += 1 #увеличиваю длинну последовательности
        if tekuschaya_dlinna > itog_dlinna:
            itog_dlinna = tekuschaya_dlinna #передаю нынешнее мах значение в итог
    else:
        tekuschaya_dlinna = 0 #при нахождении иного символа - сбрасываю счётчик

print(f"Z-1: MAX длинна X: {itog_dlinna}")



#Zadacha 2
with open('36037.txt', 'r') as moi_file:
    stroka = moi_file.read()
    # stroka = "XZZYYXYXZZY"

itog_dlinna = 0
tekuschaya_dlinna = 0
n = len(stroka)

for i in range(n):
    #не начинаются ли первые 4 символа с XZZY
    if i + 3 < n and stroka[i:i + 4] == 'XZZY': #срез чтоб не выйти за границу строки
        if tekuschaya_dlinna > itog_dlinna:
            itog_dlinna = tekuschaya_dlinna
        tekuschaya_dlinna = 0  #сбрасываю счётчик
    else:
        #если не XZZY - продолжаю
        tekuschaya_dlinna += 1
        if tekuschaya_dlinna > itog_dlinna:
            itog_dlinna = tekuschaya_dlinna

print(f"Z-2: MAX длина без XZZY: {itog_dlinna}")



#Zadacha 3
schetchik = 0
nachalo = 0

with open("46982.txt", "r") as file:
    stroka = file.read()
    #strok = "ABCEkjdaskdjhdksjdksdjElllllllllllllllllllE"

while nachalo < len(stroka):
    #начало
    if stroka[nachalo] == 'E':
        #ищу конец
        konec = nachalo + 1

        #первая E или F после начала
        while konec < len(stroka):
            tekushiy_simvol = stroka[konec]

            #проверка E ли F
            if tekushiy_simvol == 'E' or tekushiy_simvol == 'F':
                break

            #если нет E или F - продолжаю поиск
            konec += 1

        #условия
        if konec < len(stroka) and stroka[konec] == 'E' and konec - nachalo + 1 >= 12:
            schetchik += 1
            nachalo = konec #перехожу на конец группы
        else:
            #группа не подходит - иду дальше
            nachalo += 1
    else:
        #текущий символ не E - иду дальше
        nachalo += 1

print(f"Z-3: кол-во групп: {schetchik}")






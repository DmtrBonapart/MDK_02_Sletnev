#Zadacha 1
def ispolnitel_n(start, end, chislo, flag_chislo=False):
    if start == chislo: #если start равно обязательному
        flag_chislo = True

    if start > end: #если превысил - путь не подходит
        return 0

    if start == end: #если достиг end
        if flag_chislo: #встретил обязательное
            return 1
        else:
            return 0

    #все возможные пути
    itog = 0

    #прибавить 1
    itog += ispolnitel_n(start + 1, end, chislo, flag_chislo)

    #прибавить 2
    itog += ispolnitel_n(start + 2, end, chislo, flag_chislo)

    #умножить на 2
    itog += ispolnitel_n(start * 2, end, chislo, flag_chislo)

    return itog


otvet = ispolnitel_n(3, 12, 10)
print(f"кол-во программ: {otvet}")

otvet2 = ispolnitel_n(1, 4, 3)  #(1+1+1+1) (1+2+1) (1*2+1+1)
print(f"кол-во программ: {otvet2}")



#Zadacha 2
def ispolnitel_f(start, end, zapret, flag_zapret=False):
    if start == zapret: #если встретил запрещённое число
        flag_zapret = True

    if flag_zapret or start > end: #если достиг запрета или превысил
        return 0

    if start == end: #если достиг цели
        return 1

    #все возможные пути
    itog = 0

    #прибавить 1
    itog += ispolnitel_f(start + 1, end, zapret, flag_zapret)

    #сделать нечётное
    itog += ispolnitel_f(start * 2 + 1, end, zapret, flag_zapret)

    return itog


otvet = ispolnitel_f(1, 27, 26)
print(f"кол-во программ: {otvet}")

otvet2 = ispolnitel_f(1, 5, 3) #((1+1)*2+1)
print(f"кол-во программ: {otvet2}")

otvet3 = ispolnitel_f(1, 4, 2)
print(f"кол-во программ: {otvet3}")



#Zadacha 3
def ispolnitel_s(start, end, chislo, zapret, flag_chislo=False, flag_zapret=False):
    if start == chislo: #не встретил обязательное
        flag_chislo = True

    if start == zapret: #не встретил запрет
        flag_zapret = True

    if flag_zapret or start > end: #если встретил запрет или превысил
        return 0

    if start == end: #если достиг end
        if flag_chislo: #встретил обязательное
            return 1
        else:
            return 0

    itog = 0

    #прибавить 1
    itog += ispolnitel_s(start + 1, end, chislo, zapret, flag_chislo, flag_zapret)

    #прибавить 2
    itog += ispolnitel_s(start + 2, end, chislo, zapret, flag_chislo, flag_zapret)

    return itog


otvet = ispolnitel_s(2, 18, 9, 14)
print(f"кол-во программ: {otvet}")

otvet2 = ispolnitel_s(1, 5, 3, 2) # (1 + 2 + 2) и (1 + 2 + 1 + 1)
print(f"кол-во программ: {otvet2}")




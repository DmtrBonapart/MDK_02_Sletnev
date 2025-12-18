# Работа с файлами
# Задача 1
# def zadacha1(imyafaila):
#     with open(imyafaila, 'r') as f:
#         moi_ciferki = [int(line.strip()) for line in f]
#         print(moi_ciferki)
#
#     schetchik = 0
#     max_summa = 0
#
#     for i in range(len(moi_ciferki) - 1):
#         pervoe = moi_ciferki[i]
#         vtoroe = moi_ciferki[i + 1]
#
#         if (pervoe * vtoroe) % 15 == 0 and (pervoe + vtoroe) % 7 == 0:
#             schetchik += 1
#             tekuschaya_summa = pervoe + vtoroe
#             if max_summa < tekuschaya_summa:
#                 max_summa = tekuschaya_summa
#
#     print(f"Ответ: {schetchik} пар и макс. сумма элементов = {max_summa}")
#     return schetchik, max_summa
#
# zadacha1('39762.txt')


# Задача 2
# def zadacha2(imyafaila):
#     with open(imyafaila, 'r') as file:
#         chisla = file.readlines()
#         chisla = [int(el) for el in chisla]
#         max_el = 0
#         for el in chisla:
#             if str(el)[-3:] == "562":
#                 if max_el < el:
#                     max_el = el
#         c = 0
#         max_sum = 0
#         for i in range(len(chisla) - 3):
#             l = [chisla[i], chisla[i + 1], chisla[i + 2], chisla[i + 3]]
#             l5 = [el for el in l if len(str(el)) == 5]
#             lnot5 = [el for el in l if len(str(el)) != 5]
#             lcrat3 = [el for el in l if el % 3 == 0]
#             lcrat7 = [el for el in l if el % 7 == 0]
#             if len(l5) >= 1 and len(lnot5) >= 2:
#                 if len(lcrat3) < len(lcrat7):
#                     if sum(l) > max_el and sum(l) < max_el * 2:
#                         c += 1
#                         if max_sum < sum(l):
#                             max_sum = sum(l)
#     print(c, max_sum)
#
#
# zadacha2('68279.txt')



#Задача 3

def zadacha3(imyafaila):
    with open(imyafaila, "r") as f:
        moi_file = f.readlines()
        moi_file = [int(f) for f in moi_file]

    schetchik = 0
    nechet = 0
    nechet_summa = 0
    max_summa = 0
    for i in range(len(moi_file)):
        if moi_file[i] % 2 == 1:
            nechet += 1
            nechet_summa += moi_file[i]

    sred = nechet_summa / nechet
    for i in range(len(moi_file) - 1):
        a = moi_file[i]
        b = moi_file[i + 1]
        if (a % 5 == 0 or b % 5 == 0) and (a < sred or b < sred):
            schetchik += 1
            if max_summa < (a + b):
                max_summa = (a + b)
    print(schetchik, max_summa)

zadacha3("40992.txt")
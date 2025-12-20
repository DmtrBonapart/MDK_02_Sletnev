#Zadacha 1
# import csv
#
# with open("36031.csv", "r") as f:
#     t = list(csv.reader(f))
#     for i in range(len(t)):
#         t[i] = list(map(int, t[i][0].split(';')))
#
# razvetnutiy = [r[::-1] for r in t[::-1]]
#
# for i in range(len(razvetnutiy)):
#     for j in range(len(razvetnutiy[i])):
#         if i == 0 and j == 0:
#             razvetnutiy[i][j] = [razvetnutiy[i][j], ["старт"]]
#             continue
#         elif i == 0:
#             #слева j > 0
#             znachenie = razvetnutiy[i][j] + razvetnutiy[i][j - 1][0]
#             marshrut = razvetnutiy[i][j - 1][1] + ["влево"]
#             razvetnutiy[i][j] = [znachenie, marshrut]
#         elif j == 0:
#             #сверху i > 0
#             znachenie = razvetnutiy[i][j] + razvetnutiy[i - 1][j][0]
#             marshrut = razvetnutiy[i - 1][j][1] + ["вверх"]
#             razvetnutiy[i][j] = [znachenie, marshrut]
#         else:
#             #проверка при i, j > 0
#             if razvetnutiy[i - 1][j][0] >= razvetnutiy[i][j - 1][0]:
#                 #сверху
#                 znachenie = razvetnutiy[i][j] + razvetnutiy[i - 1][j][0]
#                 marshrut = razvetnutiy[i - 1][j][1] + ["вверх"]
#                 razvetnutiy[i][j] = [znachenie, marshrut]
#             else:
#                 #слева
#                 znachenie = razvetnutiy[i][j] + razvetnutiy[i][j - 1][0]
#                 marshrut = razvetnutiy[i][j - 1][1] + ["влево"]
#                 razvetnutiy[i][j] = [znachenie, marshrut]
#
# itog = razvetnutiy[-1][-1]
# print(f"\nМакс кол-во монет: {itog[0]}")
# print(f"\nПуть: {itog[1]}")


#Zadacha 2
# import csv
#
# with open("59778.csv", "r") as f:
#     file = list(csv.reader(f))
#
# l = []
# for i in range(len(file)):
#     a = (file[i][0].split(";"))
#     a = [int(el) for el in a]
#     l.append(a)
#
# count = 0
# for i in range(len(l)):
#     poisk_flag = False  #флаг, чтобы не повторяться
#     for j in range(len(l[i])):
#         if l[i].count(l[i][j]) == 4 and not poisk_flag:
#             repeat = l[i][j]
#             x = []
#             for num in l[i]:
#                 if num != repeat:
#                     x.append(num)
#             x = list(set(x))  #убираю дубликаты с помощью множества
#
#             if len(x) > 0:  # проверяю, что есть уникальные
#                 summa_repeat = 4 * repeat
#                 average_sum = sum(x) / len(x)
#                 if average_sum > summa_repeat:
#                     count += 1
#                     poisk_flag = True
#
# print(f"Число строк: {count}")



#Zadacha 3
import csv

chisla = []
with open("29666.csv", 'r') as f:
    r = csv.reader(f, delimiter=';')
    for row in r:
        #запятые на точки для преобразования
        chisla.extend([float(x.replace(',', '.')) for x in row])

max_sum = chisla[0]
n = len(chisla)

for i in range(n): #все возможные начальные позиции
    tekuschaya_sum = chisla[i]
    tekuschiy_max = chisla[i]

    for j in range(i + 1, n):
        if chisla[j] < chisla[j - 1]: #следующее число меньше предыдущего
            tekuschaya_sum += chisla[j]
            if tekuschaya_sum > tekuschiy_max:
                tekuschiy_max = tekuschaya_sum
        else: #если нарушается - прерываю
            break

    if tekuschiy_max > max_sum:
        max_sum = tekuschiy_max

print(f"МАХ сумма = {max_sum}")
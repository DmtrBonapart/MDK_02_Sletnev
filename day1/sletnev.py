# x = int(input("введите x: "))
# y = int(input("введите y: "))
#
# if 1 <= x <= 8 and 1 <= y <= 8:
#     if ((x + y) % 2) == 0:
#         print("Чёрная клетка")
#     else:
#         print("Белая клетка")
# else:
#     print("Ошибка")


#Про коня и букву Г

# x1 = int(input("Введи x первой клетки: "))
# y1 = int(input("Введи y первой клетки: "))
# x2 = int(input("Введи x второй клетки: "))
# y2 = int(input("Введи y второй клетки: "))
#
# if 1 <= x1 <= 8 and 1 <= y1 <= 8 and 1 <= x2 <= 8 and 1 <= y2 <= 8:
#     first_kletka = abs(x2 - x1) #для положительной координаты
#     second_kletka = abs(y2 - y1)
#     if (first_kletka == 2 and second_kletka == 1) or (first_kletka == 1 and second_kletka == 2):
#         print("Да, фигура может попасть с первой на вторую клетку за один ход")
#     else:
#         print("Нет, не получится")
#
# else:
#     print("Ошибка!")



#Про сумму целых от K до N

# K = int(input("K: "))
# N = int(input("N: "))
#
# summa = 0
# for i in range(K, N + 1): # +1 чтоб захватить и N тоже
#     if i % 2 == 0:
#         summa += i
#
# print(f"Сумма от {K} до {N} = {summa}")



#Про сумма чисел до ввода "0"

# itog = 0
# while True:
#     chislo = int(input("Введите любое число чтобы добавить в сумму или 0 для завершения: "))
#     if chislo == 0:
#         break
#     itog += chislo
#
# print(f"Сумма чисел: {itog}")



#Факториал N

# N = int(input("N: "))
#
# fact = 1
# for i in range(1, N + 1):
#     fact *= i
#
# print(f"Факториал {N} = {fact}")

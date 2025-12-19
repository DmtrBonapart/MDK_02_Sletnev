#Фибоначчи

# N = int(input("N = "))
#
# l = [0, 1]
#
# for i in range(N - 2):
#     new_el = l[0] + l[1]
#     l[0] = l[1]
#     l[1] = new_el
# print(l[1])



#Кузнечик

# def kuznechik(n):
#
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#
#     l = [1, 1, 2]
#
#     for i in range(n - 3):
#         new = l[0] + l[1] + l[2]
#         l = [l[1], l[2], new]  # сдвиг
#
#     return l[2]
#
#
#
# n = int(input("N: "))
# itog = kuznechik(n)
# print(f"Кол-во способов: {itog}")



#Черепашка

Coins = [
    [0, 1, 1, 1, 1, 1],
    [0, 0, 0, 0, 0, 1],
    [0, 40, 70, 0, 0, 1],
    [100, 0, 0, 0, 0, 1],
]

CoinsNew = [
    [0, 1, 10],
    [0, 1, 1],
    [0, 1, 10],
]

for i in range(len(Coins)):
    for j in range(len(Coins[i])):
        if i == 0 and j == 0:
            #стартовая точка (0, 0)
            Coins[i][j] = [Coins[i][j], [(0, 0)]]
            continue
        elif i == 0:
            #слева
            znachenie = Coins[i][j] + Coins[i][j - 1][0]
            marshrut = Coins[i][j - 1][1] + ["Вправо"]
            Coins[i][j] = [znachenie, marshrut]
        elif j == 0:
            #сверху
            znachenie = Coins[i][j] + Coins[i - 1][j][0]
            marshrut = Coins[i - 1][j][1] + ["Вниз"]
            Coins[i][j] = [znachenie, marshrut]
        else:
            #проверка на оптимальность при i, j != 0
            if Coins[i-1][j][0] >= Coins[i][j-1][0]:
                #сверху
                znachenie = Coins[i][j] + Coins[i - 1][j][0]
                marshrut = Coins[i - 1][j][1] + ["Вниз"]
                Coins[i][j] = [znachenie, marshrut]
            else:
                #слева
                znachenie = Coins[i][j] + Coins[i][j - 1][0]
                marshrut = Coins[i][j - 1][1] + ["Вправо"]
                Coins[i][j] = [znachenie, marshrut]

itog = Coins[-1][-1]
print(f"\nМакс кол-во монет: {itog[0]}")
print(f"\nПуть: {itog[1]}")





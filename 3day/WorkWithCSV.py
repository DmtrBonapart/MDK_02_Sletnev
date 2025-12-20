import csv

with open("36031.csv", "r") as f:
    t = list(csv.reader(f))
    for i in range(len(t)):
        t[i] = list(map(int, t[i][0].split(';')))

razvetnutiy = [r[::-1] for r in t[::-1]]

for i in range(len(razvetnutiy)):
    for j in range(len(razvetnutiy[i])):
        if i == 0 and j == 0:
            razvetnutiy[i][j] = [razvetnutiy[i][j], ["старт"]]
            continue
        elif i == 0:
            #слева j > 0
            znachenie = razvetnutiy[i][j] + razvetnutiy[i][j - 1][0]
            marshrut = razvetnutiy[i][j - 1][1] + ["влево"]
            razvetnutiy[i][j] = [znachenie, marshrut]
        elif j == 0:
            #сверху i > 0
            znachenie = razvetnutiy[i][j] + razvetnutiy[i - 1][j][0]
            marshrut = razvetnutiy[i - 1][j][1] + ["вверх"]
            razvetnutiy[i][j] = [znachenie, marshrut]
        else:
            #проверка при i, j > 0
            if razvetnutiy[i - 1][j][0] >= razvetnutiy[i][j - 1][0]:
                #сверху
                znachenie = razvetnutiy[i][j] + razvetnutiy[i - 1][j][0]
                marshrut = razvetnutiy[i - 1][j][1] + ["вверх"]
                razvetnutiy[i][j] = [znachenie, marshrut]
            else:
                #слева
                znachenie = razvetnutiy[i][j] + razvetnutiy[i][j - 1][0]
                marshrut = razvetnutiy[i][j - 1][1] + ["влево"]
                razvetnutiy[i][j] = [znachenie, marshrut]

itog = razvetnutiy[-1][-1]
print(f"\nМакс кол-во монет: {itog[0]}")
print(f"\nПуть: {itog[1]}")
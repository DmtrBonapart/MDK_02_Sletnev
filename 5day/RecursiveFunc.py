#Zadacha 1
# def factorial(n):
#     if n >= 1:
#         return n * factorial(n - 1)
#     return 1
#
#
# spisok = [0, 1, 2, 3, 4, 5, 10, 15]
#
# for i in spisok:
#     print(f"factorial({i}) = {factorial(i)}")


#Zadacha 2
# def remove_vowels(string):
#     glasnie = "aeiouyAEIOUY"
#     if string == "":
#         return ""
#
#     pervii_simvol = string[0]
#     ostatok_stroki = string[1:]
#
#     if pervii_simvol in glasnie:
#         return remove_vowels(ostatok_stroki)
#     else:
#         return pervii_simvol + remove_vowels(ostatok_stroki)
#
# print(remove_vowels("Privet Ya Dima"))


#Zadacha 3
# def pascal(n):
#     if n == 1:
#         return [1]
#
#     prediduschaya_stroka = pascal(n - 1)
#
#     novaya_stroka = [1] #в начале всегда - 1
#
#     for i in range(1, n-1):
#         novaya_stroka.append(prediduschaya_stroka[i - 1] + prediduschaya_stroka[i])
#
#     novaya_stroka.append(1) #в конце всегда - 1
#     return novaya_stroka
#
# print(pascal(1))
# print(pascal(2))
# print(pascal(3))
# print(pascal(4))
# print(pascal(5))



#FinalBoss
def solve(maze, row=None, col=None, path=None):
    if row is None:
        # ищу старт
        for i in range(len(maze)):
            for j in range(len(maze[0])):
                if maze[i][j] == 's':
                    # ищу пути, добавляя старт в начало
                    resultat = solve(maze, i, j, [])
                    #стартовая точка в каждом пути
                    for marshrut in resultat:
                        marshrut.insert(0, f's({i},{j})')
                    return resultat
        return []

    #если робот дошёл до x - добавляем этот путь в список правильных путей
    if maze[row][col] == 'x':
        return [path] if path else [[]]

    orig = maze[row][col] #сохраняю значение клетки
    maze[row] = maze[row][:col] + '#' + maze[row][col + 1:] #помечаю текущую клетку стеной(посещённая)

    vse_puti = []
    napravleniya = [(-1, 0, 'Вверх'), (1, 0, 'Вниз'), (0, -1, 'Влево'), (0, 1, 'Вправо')]

    for x, y, napravlenie in napravleniya:
        new_row, new_col = row + x, col + y

        #проверяю могу ли пойти на клетку
        if (0 <= new_row < len(maze) and 0 <= new_col < len(maze[0]) and
                maze[new_row][new_col] != '#'):
            #проверяем ещё дополнительный путь
            dop_puti = solve(maze, new_row, new_col, path + [napravlenie])
            vse_puti.extend(dop_puti) #добавляю доп пути в список путей

    #возвращаю ориг значение клетки, чтобы пройти другим путём
    # maze[row] = maze[row][:col] + orig + maze[row][col + 1:]
    return vse_puti

maze = [
    's----',
    '##---',
    '---##',
    '----x'
]

maze2 = [
    '--s--',
    '##---',
    '---##',
    '--x--'
]

itog = solve(maze)
itog = solve(maze2)
for i in itog:
    print(i)













































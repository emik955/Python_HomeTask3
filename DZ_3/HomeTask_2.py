# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент
# к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество
# элементов в массиве. В последующих строках записаны N целых чисел Ai. Последняя строка содержит число X

# n = 5
# 1 2 3 4 5
# x = 6
# -> 5

N = abs(int(input('Введите количество элементов списка А: ')))
A1 = input("Введите через пробел элементы списка: ").split()
A2 = list(map(int, A1))
if len(A2) != N or N == 0:
    print('Введенные элементы не соответствуют заявленному количеству!')
else:
    X = int(input('Введите число X, с которым необходимо сравнивать элементы списка: '))
    min = abs(X - A2[0])
    index = 0
    for i in range(1, N):
        count = abs(X - A2[i])
        if count < min:
            min = count
            index = i
    print(f'Число {A2[index]} в списке A наиболее близко по величине к числу {X}, их разница составляет {abs(X - A_num[index])}')
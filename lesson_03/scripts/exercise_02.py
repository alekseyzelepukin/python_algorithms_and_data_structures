# 2. Во втором массиве сохранить индексы четных элементов первого массива.
# Например, если дан массив со значениями 8, 3, 15, 6, 4, 2,
# второй массив надо заполнить значениями 0, 3, 4, 5 (помните, что индексация начинается с нуля),
# т. к. именно в этих позициях первого массива стоят четные числа.

from random import randint
from typing import List

if __name__ == '__main__':
    n: int = 10
    elements_array: List = [0 for _ in range(n)]
    even_indexes_array: List = []

    for i in range(n):
        elements_array[i] = randint(0, 9)
        if elements_array[i] % 2 == 0:
            even_indexes_array.append(i)

    print(f'Массив элементов: {elements_array}')
    print(f'Индексы четных элементов: {even_indexes_array}')
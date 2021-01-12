# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба минимальны), так и различаться.

from random import randint
from typing import List

if __name__ == '__main__':
    n: int = 10
    arr: List = [randint(-9, 9) for _ in range(n)]

    if arr[0] > arr[1]:
        min_idx_1: int = 0
        min_idx_2: int = 1
    else:
        min_idx_1 = 1
        min_idx_2 = 0

    for i in range(2, n):
        if arr[i] < arr[min_idx_1]:
            tmp_idx: int = min_idx_1
            min_idx_1 = i
            if arr[tmp_idx] < arr[min_idx_2]:
                min_idx_2: int = tmp_idx
        elif arr[i] < arr[min_idx_2]:
            min_idx_2 = i

    print(f'Массив элементов: {arr}')
    print(f'Первый наименьший элемент: {arr[min_idx_1]}')
    print(f'Второй наименьший элемент: {arr[min_idx_2]}')

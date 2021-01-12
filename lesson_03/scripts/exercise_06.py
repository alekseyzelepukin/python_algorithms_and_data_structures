# 6. В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint
from typing import List

if __name__ == '__main__':
    n: int = 4
    arr: List = [randint(0, 9) for _ in range(n)]

    min_idx: int = 0
    max_idx: int = 0

    for i in range(1, n):
        if arr[i] < arr[min_idx]:
            min_idx = i
        elif arr[i] > arr[max_idx]:
            max_idx = i

    if min_idx > max_idx:
        min_idx, max_idx = max_idx, min_idx

    amount: int = 0
    for i in range(min_idx+1, max_idx):
        amount += arr[i]

    print(f'Массив элементов: {arr}')
    print(f'Сумма элементов: {amount}')

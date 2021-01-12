# 5. В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
# Примечание к задаче: пожалуйста не путайте «минимальный» и «максимальный отрицательный».
# Это два абсолютно разных значения.

from random import randint
from typing import List

if __name__ == '__main__':
    n: int = 10
    arr: List = [randint(-9, 9) for _ in range(n)]
    i: int = 0
    idx: int = -1

    while i < n:
        if arr[i] < 0 and idx == -1:
            idx = i
        elif 0 > arr[i] > arr[idx]:
            idx = i
        i += 1

    print(f'Массив элементов: {arr}')
    print(f'Максимальный отрицательный элемент: {arr[idx]}')

# 1. В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
# Примечание: 8 разных ответов.

from typing import List

if __name__ == '__main__':
    arr: List = [0 for _ in range(8)]

    for i in range(2, 100):
        for j in range(2, 10):
            if i % j == 0:
                arr[j-2] += 1

    for idx, element in enumerate(arr, start=2):
        print(f'{idx}: {element}')

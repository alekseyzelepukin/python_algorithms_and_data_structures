# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint
from typing import List

if __name__ == '__main__':
    n: int = 10
    arr: List = [randint(0, 9) for _ in range(n)]
    num: int = arr[0]
    max_frq: int = 1

    for i in range(n-1):
        frq: int = 1
        for j in range(i+1, n):
            if arr[i] == arr[j]:
                frq += 1
        if frq > max_frq:
            max_frq = frq
            num = arr[i]

    print(f'Массив элементов: {arr}')

    if max_frq > 1:
        print(f'Число {num} встречается в массиве {max_frq} раз(а)')
    else:
        print('Все элементы массива унакальны')
# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint
from typing import List

if __name__ == '__main__':
    n: int = 6
    integers_array: List = [randint(0, 9) for _ in range(n)]
    min_element: int = 0
    max_element: int = 0

    for i in range(n):
        if integers_array[i] < integers_array[min_element]:
            min_element = i
        elif integers_array[i] > integers_array[max_element]:
            max_element = i

    print(f'Массив целых чисел: {integers_array}')

    integers_array[min_element], integers_array[max_element] = integers_array[max_element], integers_array[min_element]

    print(f'После перемены мест элементов: {integers_array}')

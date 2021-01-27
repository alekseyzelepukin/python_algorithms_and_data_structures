# 3. Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда,
# делящий его на две равные части: в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки,
# который не рассматривался на уроках (сортировка слиянием также недопустима).

import numpy as np
from random import randint
from typing import List, Optional, Union, Callable, NoReturn


def unsorted_array_median(array: List[Union[int, float]]) -> Optional[Union[int, float]]:
    """
    функция возвращает медиану несортированного массива размером 2m + 1, где m – натуральное число
    """
    median: Optional[Union[int, float]] = None
    length: int = len(array)

    if length == 0:
        pass
    elif length == 1:
        median = array[0]
    else:
        mid: int = length // 2

        for i in range(length):
            median = array[i]
            element_counter: int = 0
            same_element_counter: int = 0

            for j in range(length):
                if i != j:
                    if median > array[j]:
                        element_counter += 1
                    elif median == array[j]:
                        same_element_counter += 1

            if same_element_counter != 0:
                if element_counter < mid <= (element_counter + same_element_counter):
                    break
            else:
                if element_counter == mid:
                    break
    return median


def test(func: Callable, m: int = 5) -> NoReturn:
    n: int = 2 * m + 1
    array: List[Union[int, float]] = [randint(-100, 99) for _ in range(n)]
    assert np.median(array) == func(array)
    print(f'Test {func.__name__} for {array}: OK')


if __name__ == '__main__':
    test(unsorted_array_median)

    m: int = 5
    n: int = 2 * m + 1

    array: List[Union[int, float]] = [randint(-100, 99) for _ in range(n)]

    print(f'Исходный массив:      {array}')
    print(f'Сортированный массив: {sorted(array.copy())}')
    print(f'Медиана массива: {unsorted_array_median(array)}')

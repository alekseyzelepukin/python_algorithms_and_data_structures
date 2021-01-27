# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import uniform
from typing import List, Union, Callable, NoReturn


def merge_sort(array: List[Union[int, float]]) -> List[Union[int, float]]:
    if len(array) < 2:
        return array
    else:
        mid: int = len(array) // 2
        left_half: List[Union[int, float]]= array[:mid]
        right_half: List[Union[int, float]] = array[mid:]

        _ = merge_sort(left_half)
        _ = merge_sort(right_half)

        i: int
        j: int
        k: int

        i = j = k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1

    return array


def test(func: Callable, n: int = 10) -> NoReturn:
    array: List[Union[int, float]] = [round(uniform(0, 50), 2) for _ in range(n)]
    assert sorted(array.copy()) == func(array.copy())
    print(f'Test {func.__name__} for {array}: OK')


if __name__ == '__main__':
    test(merge_sort)

    n: int = 10

    array: List[Union[int, float]] = [round(uniform(0, 50), 2) for _ in range(n)]
    sorted_array: List[Union[int, float]] = merge_sort(array.copy())

    print(f'Исходный массив:      {array}')
    print(f'Сортированный массив: {sorted_array}')

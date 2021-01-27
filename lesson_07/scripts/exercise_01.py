# 1. Отсортируйте по убыванию методом пузырька одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100). Выведите на экран исходный и отсортированный массивы.
# Примечания:
# a. алгоритм сортировки должен быть в виде функции, которая принимает на вход массив данных,
# b. постарайтесь сделать алгоритм умнее, но помните, что у вас должна остаться сортировка пузырьком.
# Улучшенные версии сортировки, например, расчёской, шейкерная и другие в зачёт не идут.

from random import randint
from typing import List, Union, Callable, NoReturn


def bubble_sort(array: List[Union[int, float]], ascending: bool = True) -> List[Union[int, float]]:
    if len(array) < 2:
        return array

    n: int = 1

    while n < len(array):
        swap_counter: int = 0
        for i in range(len(array) - n):
            if ascending:
                if array[i] > array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swap_counter += 1
            else:
                if array[i] < array[i + 1]:
                    array[i], array[i + 1] = array[i + 1], array[i]
                    swap_counter += 1

        if swap_counter == 0:
            break

        n += 1

    return array


def test(func: Callable, ascending: bool = False, n: int = 10) -> NoReturn:
    array: List[Union[int, float]] = [randint(-100, 99) for _ in range(n)]
    assert sorted(array.copy(), reverse=~ascending) == func(array.copy(), ascending=ascending)
    print(f'Test {func.__name__} for {array}: OK')


if __name__ == '__main__':
    test(bubble_sort)

    n: int = 10

    array: List[Union[int, float]] = [randint(-100, 99) for _ in range(n)]
    sorted_array: List[Union[int, float]] = bubble_sort(array.copy(), ascending=False)

    print(f'Исходный массив:      {array}')
    print(f'Сортированный массив: {sorted_array}')

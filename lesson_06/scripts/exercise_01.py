# 1. Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков. Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание: По аналогии с эмпирической оценкой алгоритмов идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# b. написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# c. результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом. Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# d. написать общий вывод: какой из трёх вариантов лучше и почему.

import os
import sys
from random import randint
from typing import List, Dict, Any, NoReturn


# будем использовать для проверки
def show_size(x: Any, level: int = 0) -> NoReturn:
    print('\t' * level, f'type = {type(x)}, size = {sys.getsizeof(x)}, object = {x}')
    if hasattr(x, '__iter__'):
        if hasattr(x, 'items'):
            for key, value in x.items():
                show_size(key, level + 1)
                show_size(value, level + 1)
        elif not isinstance(x, str):
            for item in x:
                show_size(item, level + 1)


def memory_size(variables: Dict[str, Any], logging: bool = False) -> int:
    """
    функция подсчитывает выделенную под переменные память
    функция возвращает целое число в байтах
    logging=True - для вывода подробной информации
    """

    if logging:
        print('*' * 100)

    # variables = globals().copy()
    size: int = 0

    for obj, val in variables.items():
        if obj.startswith('__'):
            continue
        elif hasattr(val, '__loader__'):
            continue
        elif hasattr(val, '__call__'):
            continue
        size += sys.getsizeof(val)
        if logging:
            print(f'Под переменную {obj} выделено: '
                  f'{sys.getsizeof(val)} байт (накопленный итог: {size} байт)')
        if hasattr(val, '__iter__'):
            if hasattr(val, 'items'):
                for key, value in val.items():
                    size += sys.getsizeof(key)
                    size += sys.getsizeof(value)
                    if logging:
                        print(f'Под ключ {key} выделено: '
                              f'{sys.getsizeof(key)} байт (накопленный итог: {size} байт)')
                        print(f'Под значение {value} выделено: '
                              f'{sys.getsizeof(value)} байт (накопленный итог: {size} байт)')
            elif not isinstance(val, str):
                for item in val:
                    size += sys.getsizeof(item)
                    if logging:
                        print(f'Под элемент {item} выделено: '
                              f'{sys.getsizeof(item)} байт (накопленный итог: {size} байт)')
    if logging:
        print('*' * 100)

    return size


def create_matrix_in_2_loops(m: int = 3, n: int = 3) -> List[List[int]]:
    matrix: List[List[int]] = [[randint(0, 9) for _ in range(n)] for _ in range(m)]
    print(memory_size(locals(), True))
    return matrix


def create_matrix_in_1_loop(size: int = 3) -> List[List[int]]:
    matrix: List[List[int]] = list()
    tmp_arr: List[int] = list()

    for i in range(1, size**2+1):
        tmp_val: int = randint(0, 9)

        if i % size == 0:
            tmp_arr.append(tmp_val)
            matrix.append(tmp_arr)
            tmp_arr: List[int] = list()
        else:
            tmp_arr.append(tmp_val)

    print(memory_size(locals(), True))
    return matrix


def create_matix_by_recursion(m: int = 3, n: int = 3, counter: int = 0) -> List[List[int]]:
    matrix: List[List[int]] = list()
    tmp_arr: List[int] = list()

    if counter + 1 == n:
        for _ in range(m):
            tmp_arr.append(randint(0, 9))
        matrix.append(tmp_arr)
        return matrix
    else:
        for _ in range(m):
            tmp_arr.append(randint(0, 9))
        counter += 1
        matrix = create_matix_by_recursion(m, n, counter)
        matrix.append(tmp_arr)
        print(memory_size(locals(), True))
        return matrix


if __name__ == '__main__':
    print(sys.version, sys.platform)
    m1: List[List[int]] = create_matrix_in_2_loops()
    m2: List[List[int]] = create_matrix_in_1_loop()
    m3: List[List[int]] = create_matix_by_recursion()

# print(sys.version, sys.platform)
# 3.8.5 (default, Sep  4 2020, 02:22:02)
# [Clang 10.0.0 ] darwin

# m1: List[List[int]] = create_matrix_in_2_loops()
# ****************************************************************************************************
# Под переменную m выделено: 28 байт (накопленный итог: 28 байт)
# Под переменную matrix выделено: 88 байт (накопленный итог: 116 байт)
# Под элемент [3, 7, 9] выделено: 88 байт (накопленный итог: 204 байт)
# Под элемент [8, 8, 8] выделено: 88 байт (накопленный итог: 292 байт)
# Под элемент [9, 7, 6] выделено: 88 байт (накопленный итог: 380 байт)
# Под переменную n выделено: 28 байт (накопленный итог: 408 байт)
# ****************************************************************************************************
# 408

# m2: List[List[int]] = create_matrix_in_1_loop()
# ****************************************************************************************************
# Под переменную size выделено: 28 байт (накопленный итог: 28 байт)
# Под переменную matrix выделено: 88 байт (накопленный итог: 116 байт)
# Под элемент [4, 6, 4] выделено: 88 байт (накопленный итог: 204 байт)
# Под элемент [6, 5, 2] выделено: 88 байт (накопленный итог: 292 байт)
# Под элемент [7, 1, 2] выделено: 88 байт (накопленный итог: 380 байт)
# Под переменную tmp_arr выделено: 56 байт (накопленный итог: 436 байт)
# Под переменную i выделено: 28 байт (накопленный итог: 464 байт)
# Под переменную tmp_val выделено: 28 байт (накопленный итог: 492 байт)
# ****************************************************************************************************
# 492

# m3: List[List[int]] = create_matix_by_recursion()
# ****************************************************************************************************
# Под переменную m выделено: 28 байт (накопленный итог: 28 байт)
# Под переменную n выделено: 28 байт (накопленный итог: 56 байт)
# Под переменную counter выделено: 28 байт (накопленный итог: 84 байт)
# Под переменную matrix выделено: 88 байт (накопленный итог: 172 байт)
# Под элемент [0, 1, 1] выделено: 88 байт (накопленный итог: 260 байт)
# Под элемент [3, 5, 7] выделено: 88 байт (накопленный итог: 348 байт)
# Под элемент [8, 3, 5] выделено: 88 байт (накопленный итог: 436 байт)
# Под переменную tmp_arr выделено: 88 байт (накопленный итог: 524 байт)
# Под элемент 8 выделено: 28 байт (накопленный итог: 552 байт)
# Под элемент 3 выделено: 28 байт (накопленный итог: 580 байт)
# Под элемент 5 выделено: 28 байт (накопленный итог: 608 байт)
# Под переменную _ выделено: 28 байт (накопленный итог: 636 байт)
# ****************************************************************************************************
# 636

# Выводы:
# 1 из 3 вариантов алгоритмов создании квадратной матрицы (create_matrix_in_2_loops) лучше,
# так как использует ввнутри себя меньше переменных, следовательно занимаешь меньше памяти

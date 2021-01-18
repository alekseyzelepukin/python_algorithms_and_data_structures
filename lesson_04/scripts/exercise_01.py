# 1. Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания первых трех уроков.
# Примечание. Идеальным решением будет:
# a. выбрать хорошую задачу, которую имеет смысл оценивать,
# b. написать 3 варианта кода (один у вас уже есть),
# c. проанализировать 3 варианта и выбрать оптимальный,
# d. результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать, для каких N вы проводили замеры),
# e. написать общий вывод: какой из трёх вариантов лучше и почему.

import cProfile
from random import randint
from typing import List, Callable, NoReturn


def create_matrix_in_2_loops(m: int = 3, n: int = 3) -> List[List[int]]:
    matrix: List[List[int]] = [[randint(0, 9) for _ in range(n)] for _ in range(m)]
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
        return matrix


if __name__ == '__main__':
    cProfile.run('create_matix_by_recursion(100, 100)')

# create_matrix_in_2_loops

# timeit
# python -m timeit -n 100 -s "import exercise_01" "exercise_01.create_matrix_in_2_loops(3, 3)"
# 100 loops, best of 5: 7.49 usec per loop
# python -m timeit -n 100 -s "import exercise_01" "exercise_01.create_matrix_in_2_loops(10, 10)"
# 100 loops, best of 5: 66.6 usec per loop
# python -m timeit -n 100 -s "import exercise_01" "exercise_01.create_matrix_in_2_loops(100, 100)"
# 100 loops, best of 5: 6.64 msec per loop

# cProfile
# cProfile.run('create_matrix_in_2_loops(3, 3)')
# 1    0.000    0.000    0.000    0.000 exercise_01.py:14(create_matrix_in_2_loops)
# # cProfile.run('create_matrix_in_2_loops(10, 10)')
# 1    0.000    0.000    0.000    0.000 exercise_01.py:14(create_matrix_in_2_loops)
# # cProfile.run('create_matrix_in_2_loops(100, 100)')
# 1    0.000    0.000    0.016    0.016 exercise_01.py:14(create_matrix_in_2_loops)

# create_matrix_in_1_loop

# timeit
# python -m timeit -n 100 -s "import exercise_01" "exercise_01.create_matrix_in_1_loop(3)"
# 100 loops, best of 5: 7.91 usec per loop
# python -m timeit -n 100 -s "import exercise_01" "exercise_01.create_matrix_in_1_loop(10)"
# 100 loops, best of 5: 72.5 usec per loop
# python -m timeit -n 100 -s "import exercise_01" "exercise_01.create_matrix_in_1_loop(100)"
# 100 loops, best of 5: 7.17 msec per loop

# cProfile
# cProfile.run('create_matrix_in_1_loop(3)')
# 1    0.000    0.000    0.000    0.000 exercise_01.py:19(create_matrix_in_1_loop)
# cProfile.run('create_matrix_in_1_loop(10)')
# 1    0.000    0.000    0.000    0.000 exercise_01.py:19(create_matrix_in_1_loop)
# cProfile.run('create_matrix_in_1_loop(100)')
# 1    0.004    0.004    0.018    0.018 exercise_01.py:19(create_matrix_in_1_loop)

# create_matix_by_recursion

# python -m timeit -n 100 -s "import exercise_01" "exercise_01.create_matix_by_recursion(3, 3)"
# 100 loops, best of 5: 7.34 usec per loop
# python -m timeit -n 100 -s "import exercise_01" "exercise_01.create_matix_by_recursion(10, 10)"
# 100 loops, best of 5: 72 usec per loop
# python -m timeit -n 100 -s "import exercise_01" "exercise_01.create_matix_by_recursion(100, 100)"
# 100 loops, best of 5: 6.58 msec per loop

# cProfile
# cProfile.run('create_matix_by_recursion(3, 3)')
# 3/1    0.000    0.000    0.000    0.000 exercise_01.py:37(create_matix_by_recursion)
# cProfile.run('create_matix_by_recursion(10, 10)')
# 10/1    0.000    0.000    0.000    0.000 exercise_01.py:37(create_matix_by_recursion)
# cProfile.run('create_matix_by_recursion(100, 100)')
# 100/1    0.003    0.000    0.018    0.018 exercise_01.py:37(create_matix_by_recursion)

# Выводы:
# Для создания квадратной матрицы самым быстрым алгоритмом из 3 рассмотренных,
# является алгоритм с рекурсией по замерам timeit
# По замерам с помощью cProfile, самым быстрым оказался алгоритм с 2 циклами,
# при этом замеры по timeit не сильно уступают алгоритму с рекурсией
# Для реальной задачи я бы выбрал алгоритм с 2 циклами, так как тем самым,
# избавляю себе от возможных ошибок, связанных с глубиной стэка

# 2. Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Примечание. Алгоритм «Решето Эратосфена» разбирался на одном из прошлых уроков. Используйте этот код и попробуйте его улучшить/оптимизировать под задачу.
# Второй — без использования «Решета Эратосфена».
# Примечание. Вспомните классический способ проверки числа на простоту.
# Пример работы программ:
# >>> sieve(2)
# 3
# >>> prime(4)
# 7
# >>> sieve(5)
# 11
# >>> prime(1)
# 2

import numpy as np
import itertools
import math
import cProfile
from typing import List, Optional, Callable, NoReturn


def sieve(p: int) -> Optional[int]:
    if p == 0:
        return
    elif p == 1:
        return 2
    else:
        n: int = 100

        while True:
            if p < n / np.log(n):
                break
            else:
                n += 100

        numbers: List[int] = [i for i in range(n)]
        numbers[1] = 0

        for i in range(2, n):
            if numbers[i] != 0:
                j = i + i
                while j < n:
                    numbers[j] = 0
                    j += i

        prime_numbers: List[int] = [i for i in numbers if i != 0]

        return prime_numbers[p - 1]


def prime(p: int) -> Optional[int]:
    if p == 0:
        return
    elif p == 1:
        return 2
    else:
        prime_numbers: List[int] = []

        for i in itertools.count(start=2, step=1):
            for j in range(2, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    break
            else:
                prime_numbers.append(i)
                if len(prime_numbers) == p:
                    return prime_numbers[p - 1]


def test(func: Callable) -> NoReturn:
    first_10_prime_numbers: List[int] = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    for i, n in enumerate(first_10_prime_numbers, start=1):
        assert n == func(i)
        print(f'Test {func.__name__} for {i}: OK')
    print()


if __name__ == '__main__':
    test(sieve)
    test(prime)

# sieve

# timeit
# python -m timeit -n 100 -s "import exercise_02" "exercise_02.sieve(100)"
# 100 loops, best of 5: 179 usec per loop
# python -m timeit -n 100 -s "import exercise_02" "exercise_02.sieve(1000)"
# 100 loops, best of 5: 2.89 msec per loop
# python -m timeit -n 100 -s "import exercise_02" "exercise_02.sieve(10000)"
# 100 loops, best of 5: 46.4 msec per loop

# cProfile
# cProfile.run('sieve(100)')
# 1    0.000    0.000    0.000    0.000 exercise_02.py:23(sieve)
# # cProfile.run('sieve(1000)')
# 1    0.003    0.003    0.004    0.004 exercise_02.py:23(sieve)
# cProfile.run('sieve(10000)')
# 1    0.037    0.037    0.048    0.048 exercise_02.py:23(sieve)

# prime

# timeit
# python -m timeit -n 100 -s "import exercise_02" "exercise_02.prime(100)"
# 100 loops, best of 5: 292 usec per loop
# python -m timeit -n 100 -s "import exercise_02" "exercise_02.prime(1000)"
# 100 loops, best of 5: 6.32 msec per loop
# python -m timeit -n 100 -s "import exercise_02" "exercise_02.prime(10000)"
# 100 loops, best of 5: 168 msec per loop

# cProfile
# cProfile.run('prime(100)')
# 1    0.000    0.000    0.000    0.000 exercise_02.py:52(prime)
# # cProfile.run('prime(1000)')
# 1    0.007    0.007    0.008    0.008 exercise_02.py:52(prime)
# cProfile.run('prime(10000)')
# 1    0.181    0.181    0.192    0.192 exercise_02.py:52(prime)

# Выводы:
# Исходя из проведенных замеров, можно сделать вывод,
# что алгоритм с использованием Решета Эратосфена (sieve) работает существенно быстрее,
# чем алгоритм, основанный на переборе чисел и его делителей (prime)
# В реальной практике, для получения p-го простого числа я бы предпочел использовать Решето Эратосфена
# или модификации алгоритма на основе Решета Эратосфена

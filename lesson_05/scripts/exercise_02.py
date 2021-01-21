# 2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как массив, элементы которого это цифры числа.
# Например, пользователь ввёл A2 и C4F.
# Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’].
# Произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from typing import List, Dict, Deque, Callable
from collections import deque, defaultdict


def hex_add(a: str, b: str) -> List[str]:
    digit_number_a: int = len(a)
    digit_number_b: int = len(b)
    digit_number_diff: int = abs(digit_number_a - digit_number_b)

    deq_a: Deque[str] = deque(a)
    deq_b: Deque[str] = deque(b)

    if digit_number_a > digit_number_b:
        deq_b.extendleft('0' for _ in range(digit_number_diff))
    elif digit_number_b > digit_number_a:
        deq_a.extendleft('0' for _ in range(digit_number_diff))

    deq_a.reverse()
    deq_b.reverse()

    hex_digits: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    dec2hex: Dict[int, str] = defaultdict(str)
    hex2dec: Dict[str, int] = defaultdict(int)

    for index, value in enumerate(hex_digits):
        dec2hex[index] = value
        hex2dec[value] = index

    result: Deque[str] = deque()
    boost: int = 0

    for i, j in zip(deq_a, deq_b):
        dec: int = hex2dec[i] + hex2dec[j]
        digit: int = dec % 16
        if dec // 16 > 0:
            digit += boost
            result.appendleft(dec2hex[digit])
            boost = 1
        else:
            digit += boost
            result.appendleft(dec2hex[digit])
            boost = 0
    if boost > 0:
        result.appendleft(dec2hex[boost])

    return list(result)


def hex_mul(a: str, b: str) -> List[str]:
    digit_number_a: int = len(a)
    digit_number_b: int = len(b)

    deq_a: Deque[str] = deque(a)
    deq_b: Deque[str] = deque(b)

    if digit_number_b > digit_number_a:
        deq_a, deq_b = deq_b, deq_a

    deq_a.reverse()
    deq_b.reverse()

    hex_digits: List[str] = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']

    dec2hex: Dict[int, str] = defaultdict(str)
    hex2dec: Dict[str, int] = defaultdict(int)

    for index, value in enumerate(hex_digits):
        dec2hex[index] = value
        hex2dec[value] = index

    spam: List = [deque() for _ in range(max(digit_number_a, digit_number_b))]
    boost: int = 0

    for index, item in enumerate(deq_a):
        if index > 0:
            spam[index].extendleft(['0' for _ in range(index)])
        boost = 0
        for value in deq_b:
            dec: int = hex2dec[item] * hex2dec[value]
            digit: int = dec % 16
            if dec // 16 > 0:
                digit += boost
                spam[index].appendleft(dec2hex[digit])
                boost = dec // 16
            else:
                digit += boost
                spam[index].appendleft(dec2hex[digit])
                boost = 0
        if boost > 0:
            spam[index].appendleft(dec2hex[boost])

    result: str = '0'

    if len(spam) == 1:
        return list(spam)
    elif len(spam) == 2:
        return hex_add(spam[0], spam[1])
    else:
        result = '0'
        for s in spam:
            result = ''.join(hex_add(''.join(s), result))

    return list(result)


def test(func: Callable):
    add_res: List[str] = ['C', 'F', '1']
    mul_res: List[str] = ['7', 'C', '9', 'F', 'E']
    if func.__name__.endswith('add'):
        assert func('A2', 'C4F') == add_res
    elif func.__name__.endswith('add'):
        assert func('A2', 'C4F') == mul_res
    print(f'Test {func.__name__}: OK')
    print()


if __name__ == '__main__':
    test(hex_add)
    test(hex_mul)
    print(hex_add('A2', 'C4F'))
    print(hex_mul('A2', 'C4F'))

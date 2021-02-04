# 1. Определение количества различных подстрок с использованием хеш-функции.
# Пусть на вход функции дана строка. Требуется вернуть количество различных подстрок в этой строке.
# Примечания:
# * в сумму не включаем пустую строку и строку целиком;
# * без использования функций для вычисления хэша
# (hash(), sha1() или любой другой из модуля hashlib задача считается не решённой.

import hashlib
from typing import Set


def substring_count(input_string: str) -> int:
    """
    функция принимает на вход строку состоящую только из маленьких латинских букв
    функция возвращает количество различных подстрок с использованием хеш-функции
    """

    input_string: str = str(input_string.replace(' ', '')).lower()

    length: int = len(input_string)

    hash_set: Set = set()

    for i in range(length + 1):
        for j in range(i + 1, length + 1):
            s: str = input_string[i:j]
            if s != input_string:
                hash_set.add(hashlib.sha1(s.encode('utf-8')).hexdigest())

    return len(hash_set)


if __name__ == '__main__':
    some_string: str = 'spam'
    print(f'Количество различных подстрок в строке {some_string}: {substring_count(some_string)}')

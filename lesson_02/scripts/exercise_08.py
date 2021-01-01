# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.

if __name__ == '__main__':
    n: int = int(input('Введите кол-во чисел: '))
    d: int = int(input('Введите цифру, которую необходимо посчитать: '))
    counter: int = 0
    for i in range(1, n + 1):
        m: int = int(input(f'Введите число {i}: '))
        while m > 0:
            if m % 10 == d:
                counter += 1
            m = m // 10
    print(f'В введенной последовательности чисел цифра {d} встречается {counter} раз(а)')

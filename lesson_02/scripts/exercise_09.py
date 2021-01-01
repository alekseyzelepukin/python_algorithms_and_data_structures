# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

if __name__ == '__main__':
    max_number: int = 0
    sum_of_digits: int = 0
    while True:
        n: int = int(input('Введите натуральное число: '))
        if n <= 0:
            break
        m: int = n
        s: int = 0
        while n > 0:
            s += n % 10
            n //= 10
        if s > sum_of_digits:
            sum_of_digits = s
            max_number = m
    print(f'Наибольшее по сумме цифр число: {max_number} ({sum_of_digits})')

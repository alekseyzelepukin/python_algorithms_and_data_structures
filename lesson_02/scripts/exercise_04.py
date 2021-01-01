# 4. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.

if __name__ == '__main__':
    n: int = int(input('Введите кол-во элементов: '))
    element: int = 1
    amount: int = 0
    for i in range(n):
        amount += element
        element /= -2
    print(f'Сумма {n} элементов: {amount}')

# 7. Определить, является ли год, который ввел пользователь, високосным или не високосным.

if __name__ == '__main__':
    n: int = int(input('Введите год: '))
    if (n % 4 != 0) or (n % 100 == 0 and n % 400 != 0):
        print(f'Год {n} является обычным')
    else:
        print(f'Год {n} является високосным')

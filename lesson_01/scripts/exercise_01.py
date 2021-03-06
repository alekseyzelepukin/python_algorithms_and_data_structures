# 1. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака.

n1: int = 5
n2: int = 6

if __name__ == '__main__':
    # "И" оператор, копирует бит в результат только если бит присутствует в обоих операндах.
    bit_and: int = n1 & n2
    print(f'Побитовое «И» (AND) для {n1} ({bin(n1)}) и {n2} ({bin(n2)}): {bit_and} ({bin(bit_and)})')
    # "ИЛИ" оператор копирует бит, если тот присутствует в хотя бы в одном операнде.
    bit_or: int = n1 | n2
    print(f'Побитовое «ИЛИ» (OR) для {n1} ({bin(n1)}) и {n2} ({bin(n2)}): {bit_or} ({bin(bit_or)})')
    # "Исключительное ИЛИ" оператор копирует бит только если бит присутствует в одном из операндов, но не в обоих сразу.
    bit_xor: int = n1 ^ n2
    print(f'Исключающее «ИЛИ» (XOR) для {n1} ({bin(n1)}) и {n2} ({bin(n2)}): {bit_xor} ({bin(bit_xor)})')
    # Побитовое отрицание меняет биты на обратные, там где была единица становиться ноль и наоборот.
    bit_not_n1: int = ~n1
    bit_not_n2: int = ~n2
    print(f'Побитовое отрицание (NOT) для {n1} ({bin(n1)}): {bit_not_n1} ({bin(bit_not_n1)}) \ '
          f'и для {n2} ({bin(n2)}): {bit_not_n2} ({bin(bit_not_n2)})')
    # Побитовый сдвиг вправо. Значение левого операнда "сдвигается" вправо на количество бит указанных в правом
    # операнде.
    bit_shift_right: int = n1 >> 2
    print(f"""Битовый сдвиг вправо для {n1} ({bin(n1)}): {bit_shift_right} (bin{bit_shift_right}))""")
    # Побитовый сдвиг влево. Значение левого операнда "сдвигается" влево на количество бит указанных в правом операнде.
    bit_shift_left: int = n1 << 2
    print(f"""Битовый сдвиг влево для {n1} ({bin(n1)}): {bit_shift_left} (bin{bit_shift_left}))""")

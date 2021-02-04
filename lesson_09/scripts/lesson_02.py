# 2. Закодируйте любую строку по алгоритму Хаффмана.

from collections import Counter, deque
from typing import List, Dict, Deque, NoReturn


class MyNode:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right


def huffman_tree(input_string: str) -> MyNode:
    counter: Counter = Counter(input_string)

    deq: Deque = deque(sorted(counter.items(), key=lambda x: x[1]))

    while len(deq) > 1:

        weight: int = deq[0][1] + deq[1][1]
        node: MyNode = MyNode(left=deq.popleft()[0], right=deq.popleft()[0])

        for index, item in enumerate(deq):
            if weight > item[1]:
                continue
            else:
                deq.insert(index, (node, weight))
                break
        else:
            deq.append((node, weight))

    return deq[0][0]


def encode_tree(tree: MyNode, encode_table: Dict, path: str = '') -> NoReturn:
    if not isinstance(tree, MyNode):
        encode_table[tree] = path
    else:
        encode_tree(tree=tree.left,  encode_table=encode_table, path=f'{path}0')
        encode_tree(tree=tree.right, encode_table=encode_table, path=f'{path}1')


if __name__ == '__main__':
    some_string: str = 'Egg and Spam'
    encode_dict: Dict = dict()
    encode_tree(huffman_tree(some_string), encode_dict)

    encoded_list: List = []

    for element in some_string:
        encoded_list.append(encode_dict[element])

    encoded_string: str = ''.join(encoded_list)

    print(f'Оригинальная строка:   {some_string}')
    print(f'Закодированная строка: {encoded_string}')
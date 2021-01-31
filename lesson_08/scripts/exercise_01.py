# https://github.com/n1k-n1k/python-algorithms-and-data-structures--GB-interactive-2020/tree/master/unit_08_graphs
# 1. На улице встретились N друзей. Каждый пожал руку всем остальным друзьям (по одному разу). Сколько рукопожатий было?
# Примечание. Решите задачу при помощи построения графа.

from random import randint
from typing import List, Tuple


def handshakes_counter(n: int) -> (List[Tuple[int, int]], int):
    nodes: List[int] = [i for i in range(1, n + 1)]  # вершины графа - люди с номерами от 1 до n включительно
    edges: List[Tuple[int, int]] = []  # ребра графа - уникальные рукопожатия

    for i in nodes:
        for j in range(i + 1, n + 1):
            edges.append((i, j))

    return len(edges)


if __name__ == '__main__':
    n = randint(2, 9)
    m: int = handshakes_counter(n)
    print(f'На улице встретились {n} друзей.')
    print(f'Было рукопожатий: {m}.')

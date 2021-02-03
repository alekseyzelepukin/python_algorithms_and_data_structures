# 3. Написать программу, которая обходит не взвешенный ориентированный граф без петель,
# в котором все вершины связаны, по алгоритму поиска в глубину (Depth-First Search).
# Примечания:
# a. граф должен храниться в виде списка смежности;
# b. генерация графа выполняется в отдельной функции, которая принимает на вход число вершин.

from typing import Dict, Set, Optional


def dfs(graph: Dict[str, Set], start: str, visited: Optional[Set] = None) -> Set:
    if visited is None:
        visited = set()
    visited.add(start)
    for next in graph[start] - visited:
        dfs(graph, next, visited)
    return visited


if __name__ == '__main__':
    graph = {'0': set(['1', '2']),
             '1': set(['0', '3', '4']),
             '2': set(['0']),
             '3': set(['1']),
             '4': set(['2', '3'])}

    print(dfs(graph, '0'))

"""
Розробіть алгоритм Дейкстри для знаходження найкоротших шляхів у зваженому графі, 
використовуючи бінарну купу. Завдання включає створення графа, використання піраміди 
для оптимізації вибору вершин та обчислення найкоротших шляхів від початкової вершини до всіх інших.

- Програмно реалізовано алгоритм Дейкстри для знаходження найкоротшого шляху у графі з 
використанням бінарної купи (піраміди).
- У межах реалізації завдання створено граф, використано піраміду для оптимізації вибору 
вершин та виконано обчислення найкоротших шляхів від початкової вершини до всіх інших.
"""

import heapq
from math import inf
import networkx as nx

def dijkstra(g, start) -> tuple[dict[int|float], dict[object]]:
    """
    Dijkstra shortest path search implementation
    Returns 
    """
    n = g.number_of_nodes()
    distances = { node:inf for node in g.nodes()}
    distances[start] = 0
    path = { node:None for node in g.nodes()}
    queue = [(0,start)]
    heapq.heapify(queue)
    while len(queue) > 0:
        curr_path, curr = heapq.heappop(queue)
        for next_node in nx.neighbors(g,curr):
            new_path = curr_path + g[curr][next_node]["weight"]
            if new_path < distances[next_node]:
                distances[next_node] = new_path
                path[next_node] = curr
                heapq.heappush(queue,(new_path,next_node))
    return (distances, path)

#example = nx.Graph()
#example.add_edge(1,2,weight=3)
#example.add_edge(1,3,weight=2)
#example.add_edge(1,5,weight=10)
#example.add_edge(2,5,weight=5)
#example.add_edge(3,4,weight=3)
#example.add_edge(4,5,weight=4)

#d, p = dijkstra(example, 1)
#print("Shortest distances:", d)
#print("Route information:", p)


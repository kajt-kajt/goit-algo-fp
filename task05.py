"""
Використовуючи код із завдання 4 для побудови бінарного дерева, необхідно створити програму на Python, 
яка візуалізує обходи дерева: у глибину та в ширину.
Вона повинна відображати кожен крок у вузлах з різними кольорами, використовуючи 16-систему RGB 
(приклад #1296F0). Кольори вузлів мають змінюватися від темних до світлих відтінків, 
залежно від послідовності обходу. Кожен вузол при його відвідуванні має отримувати унікальний колір, 
який візуально відображає порядок обходу.
👉🏻 Примітка. Використовуйте стек та чергу, НЕ рекурсію

- Програмно реалізовано алгоритми DFS і BFS для візуалізації обходу дерева в глибину та в ширину. 
Використано стек та чергу.
- Кольори вузлів змінюються від темних до світлих відтінків залежно від порядку обходу.
"""

import uuid
from collections import deque
from colour import Color
import networkx as nx
import matplotlib.pyplot as plt


class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color # Додатковий аргумент для зберігання кольору вузла
        self.id = str(uuid.uuid4()) # Унікальний ідентифікатор для кожного вузла


def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val) # Використання id та збереження значення вузла
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph


def draw_tree(tree_root):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def draw_tree_traversal_order(tree_root, traversal_algorithm, start):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)} # Використовуйте значення вузла для міток

    colour1 = Color("lightblue")
    color_gradient = list(colour1.range_to(Color("darkblue"),tree.number_of_nodes()))

    traversal_order = traversal_algorithm(tree, start)
    for node, color in zip(traversal_order, color_gradient):
        tree.nodes[node]["color"] = color.rgb

    colors = [node[1]['color'] for node in tree.nodes(data=True)]

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)
    plt.show()


def bfs(g, start) -> list[str]:
    """
    Let's generate traversal order based on BFS algorithm
    """
    visited = { node: False for node in g.nodes() }
    result = []
    queue = deque()
    queue.append(start)
    while len(queue) > 0:
        current = queue.popleft()
        if not visited[current]:
            visited[current] = True
            result.append(current)
            queue.extend(nx.neighbors(g, current))
    return result


def dfs(g, start) -> list[str]:
    """
    Let's generate traversal order based on DFS algorithm
    """
    visited = { node: False for node in g.nodes() }
    result = []
    stack = deque()
    stack.append(start)
    while len(stack) > 0:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            stack.extend(nx.neighbors(g, current))
            result.append(current)
    return result


# Створення дерева
root = Node(0)
root.left = Node(4)
root.left.left = Node(5)
root.left.right = Node(10)
root.right = Node(1)
root.right.left = Node(3)

# Відображення дерева
draw_tree_traversal_order(root, bfs, root.id)
#draw_tree_traversal_order(root, dfs, root.id)


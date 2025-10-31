from collections import deque
from directed_graph import DirectedGraph

def bfs(graph, start_vertex):
    """
    Обход ориентированного графа в ширину (Breadth-First Search).

    :param graph: Объект DirectedGraph.
    :param start_vertex: Начальная вершина для обхода.
    :return: Список вершин в порядке обхода.
    """
    visited = set()
    queue = deque([start_vertex])
    result = []

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.add(vertex)
            result.append(vertex)

            # Добавляем непосещённых соседей в очередь
            for neighbor in graph.get_neighbors(vertex):
                if neighbor not in visited:
                    queue.append(neighbor)

    return result

# Тестирование
if __name__ == "__main__":
    print("--- Тестирование BFS ---")
    dg = DirectedGraph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'A')]
    for edge in edges:
        dg.add_edge(edge[0], edge[1])

    start = 'A'
    bfs_result = bfs(dg, start)
    print(f"Обход в ширину из '{start}': {bfs_result}")
    print("--- Тестирование BFS завершено ---\n")
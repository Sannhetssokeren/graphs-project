def create_list(edges):
    """
    Создает список смежности для ориентированного графа из списка ребер.

    :param edges: Список кортежей (from_vertex, to_vertex).
    :return: Словарь, где ключи - вершины, значения - множества соседей.
    """
    graph = {}
    for edge in edges:
        from_vertex, to_vertex = edge
        # Убедимся, что обе вершины существуют
        if from_vertex not in graph:
            graph[from_vertex] = set()
        if to_vertex not in graph:
            graph[to_vertex] = set()

        # Добавим ребро
        graph[from_vertex].add(to_vertex)

    return graph

def add_vertex_list(graph, new_vertex):
    """
    Добавляет новую вершину в список смежности.

    :param graph: Словарь (список смежности).
    :param new_vertex: Новая вершина для добавления.
    """
    if new_vertex not in graph:
        graph[new_vertex] = set()

def add_edge_list(graph, from_vertex, to_vertex):
    """
    Добавляет направленное ребро в список смежности.

    :param graph: Словарь (список смежности).
    :param from_vertex: Исходная вершина.
    :param to_vertex: Конечная вершина.
    """
    # Убедимся, что обе вершины существуют в графе
    add_vertex_list(graph, from_vertex)
    add_vertex_list(graph, to_vertex)
    # Добавим ребро
    graph[from_vertex].add(to_vertex)

# Пример использования
if __name__ == "__main__":
    print("--- Тестирование списка смежности ---")
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]

    graph = create_list(edges)
    print("Список смежности:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {neighbors}")

    add_vertex_list(graph, 'E')
    print("\nПосле добавления вершины 'E':")
    print("Список смежности:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {neighbors}")

    add_edge_list(graph, 'D', 'E')
    print("\nПосле добавления ребра D -> E:")
    print("Список смежности:")
    for vertex, neighbors in graph.items():
        print(f"{vertex}: {neighbors}")
    print("--- Тестирование списка смежности завершено ---\n")
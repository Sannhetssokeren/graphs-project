class DirectedGraph:
    def __init__(self):
        """
        Инициализирует пустой ориентированный граф.
        Используем словарь для представления графа (список смежности).
        """
        self.graph = {}

    def add_vertex(self, vertex):
        """
        Добавляет вершину в граф.

        :param vertex: Значение вершины.
        """
        if vertex not in self.graph:
            self.graph[vertex] = set() # Используем set для хранения соседей, чтобы избежать дубликатов

    def add_edge(self, from_vertex, to_vertex):
        """
        Добавляет направленное ребро из from_vertex в to_vertex.

        :param from_vertex: Исходная вершина.
        :param to_vertex: Конечная вершина.
        """
        # Убедимся, что обе вершины существуют в графе
        self.add_vertex(from_vertex)
        self.add_vertex(to_vertex)
        # Добавим ребро (to_vertex) в список соседей from_vertex
        self.graph[from_vertex].add(to_vertex)

    def get_vertices(self):
        """Возвращает список всех вершин."""
        return list(self.graph.keys())

    def get_neighbors(self, vertex):
        """Возвращает список соседей вершины."""
        return list(self.graph.get(vertex, set()))

# Тестирование
if __name__ == "__main__":
    print("--- Тестирование DirectedGraph ---")
    dg = DirectedGraph()

    # Добавляем вершины
    vertices = ['A', 'B', 'C', 'D']
    for v in vertices:
        dg.add_vertex(v)
        print(f"Добавлена вершина: {v}")

    # Добавляем ребра
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'A')]
    for edge in edges:
        dg.add_edge(edge[0], edge[1])
        print(f"Добавлено ребро: {edge[0]} -> {edge[1]}")

    # Выводим граф
    print("\nСтруктура графа (список смежности):")
    for vertex in dg.get_vertices():
        print(f"{vertex}: {dg.get_neighbors(vertex)}")

    print("--- Тестирование DirectedGraph завершено ---\n")
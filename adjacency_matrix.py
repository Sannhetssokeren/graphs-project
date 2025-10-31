def create_matrix(vertices, edges):
    """
    Создает матрицу смежности для ориентированного графа из списка вершин и ребер.

    :param vertices: Список вершин.
    :param edges: Список кортежей (from_vertex, to_vertex).
    :return: Матрица смежности (список списков) и словарь индексов.
    """
    vertex_to_index = {v: i for i, v in enumerate(vertices)}
    n = len(vertices)
    matrix = [[0] * n for _ in range(n)]

    for edge in edges:
        from_idx = vertex_to_index[edge[0]]
        to_idx = vertex_to_index[edge[1]]
        matrix[from_idx][to_idx] = 1 # 1 означает наличие ребра

    return matrix, vertex_to_index

def add_vertex_matrix(matrix, vertex_to_index, new_vertex):
    """
    Добавляет новую вершину в матрицу смежности и обновляет словарь индексов.

    :param matrix: Текущая матрица смежности.
    :param vertex_to_index: Словарь соответствия вершин индексам.
    :param new_vertex: Новая вершина для добавления.
    """
    if new_vertex in vertex_to_index:
        print(f"Вершина '{new_vertex}' уже существует.")
        return

    n = len(matrix)
    # Добавляем новую строку (для новой вершины)
    matrix.append([0] * (n + 1))
    # Добавляем новый столбец ко всем старым строкам
    for row in matrix[:-1]: # Все строки, кроме новой
        row.append(0)

    # Обновляем словарь
    vertex_to_index[new_vertex] = n

def add_edge_matrix(matrix, vertex_to_index, from_vertex, to_vertex):
    """
    Добавляет направленное ребро в матрицу смежности.

    :param matrix: Матрица смежности.
    :param vertex_to_index: Словарь соответствия вершин индексам.
    :param from_vertex: Исходная вершина.
    :param to_vertex: Конечная вершина.
    """
    from_idx = vertex_to_index.get(from_vertex)
    to_idx = vertex_to_index.get(to_vertex)

    if from_idx is None or to_idx is None:
        print(f"Ошибка: Одна из вершин ('{from_vertex}' или '{to_vertex}') не найдена в индексах.")
        return

    matrix[from_idx][to_idx] = 1

# Пример использования
if __name__ == "__main__":
    print("--- Тестирование матрицы смежности ---")
    vertices = ['A', 'B', 'C', 'D']
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D')]

    matrix, v_to_idx = create_matrix(vertices, edges)
    print("Матрица смежности:")
    for row in matrix:
        print(row)
    print(f"Словарь индексов: {v_to_idx}")

    add_vertex_matrix(matrix, v_to_idx, 'E')
    print("\nПосле добавления вершины 'E':")
    print("Матрица смежности:")
    for row in matrix:
        print(row)
    print(f"Словарь индексов: {v_to_idx}")

    add_edge_matrix(matrix, v_to_idx, 'D', 'E')
    print("\nПосле добавления ребра D -> E:")
    print("Матрица смежности:")
    for row in matrix:
        print(row)
    print("--- Тестирование матрицы смежности завершено ---\n")
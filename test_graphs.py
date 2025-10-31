from directed_graph import DirectedGraph
from graph_traversals import bfs
from adjacency_matrix import create_matrix, add_vertex_matrix, add_edge_matrix
from adjacency_list import create_list, add_vertex_list, add_edge_list

def test_all():
    print("--- Тестирование всех компонентов ---")

    # 1. DirectedGraph
    print("\n1. Тестирование DirectedGraph:")
    dg = DirectedGraph()
    edges = [('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), ('D', 'A')]
    for edge in edges:
        dg.add_edge(edge[0], edge[1])

    print(f"  Вершины: {dg.get_vertices()}")
    print(f"  Соседи A: {dg.get_neighbors('A')}")
    print(f"  BFS из A: {bfs(dg, 'A')}")

    # 2. Матрица смежности
    print("\n2. Тестирование матрицы смежности:")
    vertices = ['A', 'B', 'C', 'D']
    matrix, v_to_idx = create_matrix(vertices, edges)
    print(f"  Матрица: {matrix}")
    print(f"  Индексы: {v_to_idx}")

    add_vertex_matrix(matrix, v_to_idx, 'E')
    print(f"  После добавления E - Матрица: {matrix}")
    print(f"  После добавления E - Индексы: {v_to_idx}")

    add_edge_matrix(matrix, v_to_idx, 'D', 'E')
    print(f"  После добавления D->E - Матрица: {matrix}")

    # 3. Список смежности
    print("\n3. Тестирование списка смежности:")
    graph_list = create_list(edges)
    print(f"  Список: {graph_list}")

    add_vertex_list(graph_list, 'E')
    print(f"  После добавления E - Список: {graph_list}")

    add_edge_list(graph_list, 'D', 'E')
    print(f"  После добавления D->E - Список: {graph_list}")

    print("\n--- Тестирование всех компонентов завершено ---")

if __name__ == "__main__":
    test_all()
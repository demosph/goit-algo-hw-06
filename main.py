import networkx as nx
import matplotlib.pyplot as plt

# Створення графа
G = nx.Graph()

# Додавання вершин
G.add_nodes_from([
    (1, {'name': 'Intersection A'}),
    (2, {'name': 'Intersection B'}),
    (3, {'name': 'Intersection C'}),
    (4, {'name': 'Intersection D'}),
    (5, {'name': 'Intersection E'}),
    (6, {'name': 'Intersection F'}),
])

# Додавання ребер та їх атрибутів
G.add_edges_from([
    (1, 2, {'distance': 5, 'cost': 2}),
    (1, 3, {'distance': 8, 'cost': 3}),
    (2, 4, {'distance': 10, 'cost': 4}),
    (2, 5, {'distance': 7, 'cost': 2}),
    (3, 6, {'distance': 6, 'cost': 3}),
    (4, 5, {'distance': 4, 'cost': 1}),
    (5, 6, {'distance': 9, 'cost': 4}),
    (5, 3, {'distance': 3, 'cost': 1})
])

# Визначення шляхів з використанням DFS
dfs_paths = list(nx.all_simple_paths(G, source=1, target=6))

# Визначення шляхів з використанням BFS
bfs_paths = list(nx.all_shortest_paths(G, source=1, target=6))

# Знаходження найкоротших шляхів від кожної вершини до всіх інших
all_shortest_paths = {}
for node in G.nodes:
    paths = nx.single_source_dijkstra_path(G, source=node)
    all_shortest_paths[node] = paths

# Аналіз основних характеристик графа
print("Number of nodes:", G.number_of_nodes())
print("Number of edges:", G.number_of_edges())
for node in G.nodes:
    print(f"Degree of node {node}: {G.degree[node]}")

print("Average degree:", G.number_of_edges() / G.number_of_nodes())

# Відображення шляхів, знайдених за допомогою DFS та BFS
print("\nDFS Paths:", dfs_paths)
print("BFS Paths:", bfs_paths, "\n")

# Відображення найкоротших шляхів, знайдених за домогою алгоритму Дейкстри
for start_node, paths in all_shortest_paths.items():
    print(f"Shortest paths from {start_node}: {paths}")

# Візуалізація графа
pos = nx.spring_layout(G)
nx.draw(G, pos, with_labels=True, font_weight='bold', node_size=700, node_color='skyblue', font_color='black', font_size=8)
edge_labels = {(i, j): f"Dist: {d['distance']}\nCost: {d['cost']}" for i, j, d in G.edges(data=True)}
nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_color='red')

# Розміщення міток вершин вище вершин
node_labels = {node: data['name'] for node, data in G.nodes(data=True)}
node_label_positions = {k: (v[0], v[1] + 0.1) for k, v in pos.items()}  # Збільшення y-координати
nx.draw_networkx_labels(G, node_label_positions, labels=node_labels, font_color='black')

plt.show()
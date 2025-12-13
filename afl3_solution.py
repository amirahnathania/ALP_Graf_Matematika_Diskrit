from graf import Graf
import networkx as nx
import matplotlib.pyplot as plt

# =================================================
# SOAL 1 — Graf Tak Berarah, Derajat, Konektivitas
# =================================================
print("PROGRAM AFL3 DIMULAI")

g1 = Graf()

# Menambahkan node
nodes1 = ['A', 'B', 'C', 'D', 'E', 'F']
for n in nodes1:
    g1.add_node(n)

# Menambahkan edge
edges1 = [
    ('A', 'B'),
    ('A', 'C'),
    ('B', 'D'),
    ('C', 'E'),
    ('D', 'E'),
    ('E', 'F'),
    ('C', 'F')
]

for u, v in edges1:
    g1.add_edge(u, v)

# a. Visualisasi graf
print("a. Visualisasi Graf")
g1.visualize_graph()

# b. Derajat setiap simpul
print("b. Derajat setiap simpul:")
for n in nodes1:
    print(f"Derajat {n} =", g1.node_degree(n))

# c. Cycle
print("c. Cycle pada graf:")
print("Contoh cycle: A-C-E-D-B-A dan C-E-F-C")

# d. Konektivitas
print("d. Graf terhubung:", g1.is_connected())


# =================================================
# SOAL 2 — Graf Terarah Berbobot, Path, Cycle
# =================================================
print("\n=== AFL-3 SOAL 2 ===")

# Graf terarah menggunakan NetworkX (pengembangan konsep Graf)
g2 = nx.DiGraph()

edges2 = [
    (1, 3, 4),
    (3, 2, 6),
    (2, 4, 3),
    (4, 5, 2),
    (5, 3, 5)
]

for u, v, w in edges2:
    g2.add_edge(u, v, weight=w)

# a. Visualisasi graf terarah
print("a. Visualisasi Graf Terarah")
pos = nx.spring_layout(g2)
nx.draw(g2, pos, with_labels=True, node_size=1500, arrows=True)
nx.draw_networkx_edge_labels(
    g2,
    pos,
    edge_labels=nx.get_edge_attributes(g2, 'weight')
)
plt.show()

# b. Path dari 1 ke 5
print("b. Path dari 1 ke 5:")
if nx.has_path(g2, 1, 5):
    path_1_5 = nx.shortest_path(g2, 1, 5, weight='weight')
    print("Path:", path_1_5)
else:
    print("Tidak ada path")

# c. Cycle
print("c. Cycle pada graf:")
cycles = list(nx.simple_cycles(g2))
print(cycles)

# d. Strongly connected
print("d. Strongly connected:", nx.is_strongly_connected(g2))

# e. Jalur terpendek 1 ke 5
print("e. Jalur terpendek dari 1 ke 5:")
print("Jarak:", nx.shortest_path_length(g2, 1, 5, weight='weight'))


# =================================================
# SOAL 3 — BFS, DFS, dan Dijkstra
# =================================================
print("\n=== AFL-3 SOAL 3 ===")

g3 = Graf()

edges3 = [
    ('A', 'B', 2),
    ('A', 'C', 5),
    ('B', 'D', 4),
    ('B', 'E', 6),
    ('C', 'F', 3),
    ('D', 'G', 2),
    ('E', 'F', 4),
    ('F', 'G', 1)
]

for u, v, w in edges3:
    g3.add_edge(u, v, weight=w)

# a. Visualisasi graf
print("a. Visualisasi Graf")
g3.visualize_graph()

# b. BFS dari A
print("b. BFS dari A:")
bfs_order = list(nx.bfs_tree(g3.graph, 'A'))
print(bfs_order)

# c. DFS dari A
print("c. DFS dari A:")
dfs_order = list(nx.dfs_preorder_nodes(g3.graph, 'A'))
print(dfs_order)

# d. Dijkstra
print("d. Dijkstra dari A:")
distances = nx.single_source_dijkstra_path_length(g3.graph, 'A')
print("Jarak minimum dari A ke semua simpul:")
for node, dist in distances.items():
    print(f"A ke {node} = {dist}")

print("Jalur terpendek dari A ke G:")
print(nx.shortest_path(g3.graph, 'A', 'G', weight='weight'))

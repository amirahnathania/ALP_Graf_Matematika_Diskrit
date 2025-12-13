from graf import Graf

g = Graf()

g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
g.add_node(5)

g.add_edge(1, 2, weight=4.5)
g.add_edge(1, 3, weight=3.2)
g.add_edge(2, 4, weight=2.7)
g.add_edge(3, 4, weight=1.8)
g.add_edge(3, 5, weight=2.7)

print("Jalur terpendek:", g.shortest_path(1, 5))
print("Jarak terpendek:", g.shortest_distance(1, 5))
print("Graf terhubung:", g.is_connected())

g.visual_shortest_path(1, 5)

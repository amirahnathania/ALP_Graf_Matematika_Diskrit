import networkx as nx
import matplotlib.pyplot as plt

class Graf:
    def __init__(self):
        self.graph = nx.Graph()

    def add_node(self, node):
        self.graph.add_node(node)

    def add_edge(self, node1, node2, weight=1):
        self.graph.add_edge(node1, node2, weight=weight)

    def visualize_graph(self):
        pos = nx.spring_layout(self.graph)
        weights = nx.get_edge_attributes(self.graph, 'weight')

        nx.draw(self.graph, pos, with_labels=True, node_size=1500)
        nx.draw_networkx_edge_labels(self.graph, pos, edge_labels=weights)

        plt.show()

    def shortest_path(self, start, end):
        return nx.shortest_path(
            self.graph,
            source=start,
            target=end,
            weight='weight'
        )

    def visual_shortest_path(self, start, end):
        pos = nx.spring_layout(self.graph)
        path = self.shortest_path(start, end)

        nx.draw(self.graph, pos, with_labels=True, node_color='lightgrey', node_size=1500)

        edges = list(zip(path, path[1:]))
        nx.draw_networkx_nodes(self.graph, pos, nodelist=path, node_color='orange')
        nx.draw_networkx_edges(self.graph, pos, edgelist=edges, edge_color='red', width=3)

        plt.show()

    # 1. Mengecek apakah graf terhubung
    def is_connected(self):
        return nx.is_connected(self.graph)

    # 2. Mengambil derajat sebuah node
    def node_degree(self, node):
        return self.graph.degree[node]

    # 3. Mengambil semua node
    def get_nodes(self):
        return list(self.graph.nodes)

    # 4. Mengambil semua edge beserta bobot
    def get_edges(self):
        return list(self.graph.edges(data=True))

    # 5. Menghitung jarak terpendek (total bobot)
    def shortest_distance(self, start, end):
        return nx.shortest_path_length(
            self.graph,
            source=start,
            target=end,
            weight='weight'
        )

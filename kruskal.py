from collections import defaultdict

class Graph:

    def __init__(self):
        self.graph = []
        self.node_map = defaultdict(int)
        self.edges_set = set()
        self.actionStep = 0

    def add_vertex(self, node):
        if node not in self.node_map:
            self.node_map[node] = len(self.node_map)

    def add_edge(self, u, v, w):
        if (u, v) not in self.edges_set and (v, u) not in self.edges_set:
            self.graph.append((u, v, w))
            self.edges_set.add((u, v))

    def find(self, parent, node):
        if parent[node] == node:
            return node
        return self.find(parent, parent[node])

    def union(self, parent, rank, x, y):
        xroot = self.find(parent, x)
        yroot = self.find(parent, y)

        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0
        self.graph.sort(key=lambda item: item[2])
        parent = {}
        rank = {}
        for node in self.node_map:
            parent[node] = node
            rank[node] = 0

        while e < len(self.node_map) - 1:
            u, v, w = self.graph[i]
            i += 1

            self.actionStep = self.actionStep + 1
            print(f"Checking edge {u} - {v}" + " -> Step: " + str(self.actionStep))
            x = self.find(parent, u)
            y = self.find(parent, v)

            if x != y:
                e += 1
                result.append((u, v, w))
                self.union(parent, rank, x, y)
            else:
                print(f"Edge {u} - {v} is not in the spanning tree")

        print("Edges in the minimum spanning tree:")
        for u, v, weight in result:
            print(f"{u} -- {v} == {weight}")

def emanuel():
    g = Graph()
    for node in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
        g.add_vertex(node)

    g.add_edge('A', 'H', 2)
    g.add_edge('A', 'I', 3)
    g.add_edge('A', 'C', 11)
    g.add_edge('F', 'A', 10)
    g.add_edge('F', 'I', 4)
    g.add_edge('F', 'E', 7)
    g.add_edge('G', 'I', 12)
    g.add_edge('G', 'E', 8)
    g.add_edge('B', 'C', 5)
    g.add_edge('B', 'D', 13)
    g.add_edge('C', 'H', 9)
    g.add_edge('H', 'D', 1)
    g.add_edge('H', 'I', 6)
    g.add_edge('I', 'G', 12)
    g.add_edge('D', 'B', 13)
    g.add_edge('E', 'F', 7)
    g.add_edge('E', 'G', 8)

    g.kruskal()

import sys
def fromCLIInput(args):
    graph = Graph()
    for arg in args:
        if arg.startswith("nodes="):
            splitOnComma = arg.split("=")[1].replace("\"", "").split(", ")
            for nodeNeighboorPair in splitOnComma:
                if ":" in nodeNeighboorPair:
                    nodeNeighboorSplit = nodeNeighboorPair.split(": ")
                    node = nodeNeighboorSplit[0]
                    graph.add_vertex(node)
                    neighbors = nodeNeighboorSplit[1]

                    if neighbors is not None:
                        neighboorSplit = neighbors.split(" ")
                        for i in range(0, len(neighboorSplit), 2):
                            graph.add_edge(node, neighboorSplit[i], int(neighboorSplit[i + 1]))
                else:
                    graph.add_vertex(nodeNeighboorPair)
    graph.kruskal()

if __name__ == '__main__':
    cliFound = False
    for arg in sys.argv:
        if arg.startswith("start=") or arg.startswith("nodes="):
            fromCLIInput(sys.argv)
            cliFound = True

    if not cliFound:
        emanuel()


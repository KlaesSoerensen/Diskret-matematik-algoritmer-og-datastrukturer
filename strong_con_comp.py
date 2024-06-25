import sys
from collections import defaultdict

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)
        self.Time = 0
        self.node_index = {}
        self.index_node = {}

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def SCCUtil(self, u, low, disc, stack_member, stack, collectionList) -> []:
        disc[u] = self.Time
        low[u] = self.Time
        self.Time += 1
        stack_member[u] = True
        stack.append(u)

        for v in self.graph[u]:
            if disc[v] == -1:
                self.SCCUtil(v, low, disc, stack_member, stack, collectionList)
                low[u] = min(low[u], low[v])
            elif stack_member[v]:
                low[u] = min(low[u], disc[v])

        w = -1
        popped = []
        if low[u] == disc[u]:
            while w != u:
                w = stack.pop()
                popped.append(self.index_node[w])
                stack_member[w] = False
        collectionList.append(popped)
        

    def SCC(self):
        disc = [-1] * self.V
        low = [-1] * self.V
        stack_member = [False] * self.V
        stack = []
        collected = []

        for i in range(self.V):
            if disc[i] == -1:
                self.SCCUtil(i, low, disc, stack_member, stack, collected)

        collected = [array for array in collected if array]
        print("Amount of SCCs: ", len(collected))
        print(collected)

def parse_input(input_str):
    nodes_str = input_str.strip().replace("\"", "").split(",")
    graph = defaultdict(list)
    nodes = set()

    for nodeNeighboorPair in nodes_str:
        if ":" in nodeNeighboorPair:
            node, edges = nodeNeighboorPair.split(":")
            node = node.strip()
            nodes.add(node)
            edges = edges.strip().split(" ")
            for edge in edges:
                if edge:
                    graph[node].append(edge)
                    nodes.add(edge)
        else:
            node = nodeNeighboorPair.strip()
            nodes.add(node)
            graph[node] = []

    node_list = list(nodes)
    node_index = {node: i for i, node in enumerate(node_list)}
    index_node = {i: node for i, node in enumerate(node_list)}

    g = Graph(len(node_list))
    g.node_index = node_index
    g.index_node = index_node

    for node in graph:
        for neighbor in graph[node]:
            g.add_edge(node_index[node], node_index[neighbor])

    return g

if __name__ == "__main__":
    input_str = None
    start_node = None

    for arg in sys.argv:
        if arg.startswith("nodes="):
            input_str = arg.split("=")[1]
        elif arg.startswith("start="):
            start_node = arg.split("=")[1].strip()

    if input_str:
        g = parse_input(input_str)
        print("Strongly Connected Components in the given graph:")
        g.SCC()


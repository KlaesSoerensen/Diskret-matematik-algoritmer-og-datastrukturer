import sys

class Graph:
    def __init__(self, vertices, start_node='A'):
        self.V = vertices
        self.graph = {chr(ord(start_node) + i): {} for i in range(vertices)}

    def min_key(self, key, mst_set):
        min_value = sys.maxsize
        min_vertex = None

        for v in key:
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
                min_vertex = v

        return min_vertex

    def prim_jarnik(self, start_node):
        parent = {v: None for v in self.graph}
        key = {v: sys.maxsize for v in self.graph}
        mst_set = {v: False for v in self.graph}

        key[start_node] = 0

        for _ in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in self.graph[u]:
                weight = self.graph[u][v]
                if (
                    not mst_set[v]
                    and weight < key[v]
                ):
                    key[v] = weight
                    parent[v] = u

        return parent

# Example usage:

startNode = 'A'
g = Graph(9,startNode)
g.graph = {
    'A': {'C': 11, 'F': 10, 'H': 2,'I':3},
    'B': {'C':5,'D':13 },
    'C': {'A':11,'B': 5,'H':9},
    'D': {'B':13,'H':1},
    'E': {'F':7,'G':8},
    'F':{'A':10,'E':7,'I':4},
    'G':{'E':8,'I':12},
    'H':{'A':2,'C':9,'D':1,'I':6},
    'I':{'A':3,'F':4,'G':12,'H':6}
}

import sys
for arg in sys.argv:
    if arg.startswith("start="):
        startNode = arg.split("=")[1].strip()
    
    elif arg.startswith("nodes="):
        nodes = arg.split("=")[1].strip().replace("\"", "").split(",") # a: e 12, b: a 12 c 12, c: f d, d: d f, e: b h, f: i, g: e, h: g i c, i: j, j: f
        tempGraph: dict[str: dict[str, int]] = dict()

        for nodeNeighboorPair in nodes: # a: e 12 b 4

            if ":" in nodeNeighboorPair:
                node, edges = nodeNeighboorPair.split(":") # a: e 12, b: a 12 c 12
                edges = edges.strip().split(" ")
                tempGraph[node] = dict()
                for i in range(0, len(edges), 2): # a 12 c 12
                    edge = edges[i]
                    edgeWeight = edges[i+1]
                    tempGraph[node][edge] = int(edgeWeight)
            else:
                tempGraph[nodeNeighboorPair] = dict()

        g = Graph(len(tempGraph),startNode)
        g.graph = tempGraph


mst = g.prim_jarnik(startNode)

print("Edge   Weight")
for v in mst:
    if mst[v] is not None:
        print(mst[v], "-", v, "  ", g.graph[mst[v]][v])

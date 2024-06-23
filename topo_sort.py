from collections import defaultdict

# class to represent a graph object
class Graph:
    # Constructor
    def __init__(self, vertices):
        # A dictionary to represent an adjacency list
        self.adjList = defaultdict(list)
        # stores in-degree of a vertex
        # initialize in-degree of each vertex by 0
        self.indegree = defaultdict(int)
        # add vertices to the graph
        self.vertices = vertices
        # add edges to the graph
        for vertex in vertices:
            self.adjList[vertex] = []
            self.indegree[vertex] = 0
 
    # function to add an edge to the graph
    def addEdge(self, src, dest):
        self.adjList[src].append(dest)
        self.indegree[dest] += 1

# Recursive function to find all topological orderings of a given DAG
def findAllTopologicalOrders(graph, path, discovered, N):
    # do for every vertex
    for v in graph.vertices:
        # proceed only if in-degree of current node is 0 and current node is not processed yet
        if graph.indegree[v] == 0 and not discovered[v]:
            # for every adjacent vertex u of v, reduce in-degree of u by 1
            for u in graph.adjList[v]:
                graph.indegree[u] -= 1
            # include current node in the path and mark it as discovered
            path.append(v)
            discovered[v] = True
            # recur
            findAllTopologicalOrders(graph, path, discovered, N)
            # backtrack: reset in-degree information for the current node
            for u in graph.adjList[v]:
                graph.indegree[u] += 1
            # backtrack: remove current node from the path and mark it as undiscovered
            path.pop()
            discovered[v] = False
    # print the topological order if all vertices are included in the path
    if len(path) == N:
        print(path)

# Print all topological orderings of a given DAG
def printAllTopologicalOrders(graph):
    # get number of nodes in the graph
    N = len(graph.vertices)
    # create an auxiliary space to keep track of whether vertex is discovered
    discovered = defaultdict(bool)
    # list to store the topological order
    path = []
    # find all topological ordering and print them
    findAllTopologicalOrders(graph, path, discovered, N)

import sys
# Driver code
if __name__ == '__main__':
    # List of graph edges as per above diagram
    edges = [('b', 'a'), ('b', 'c'), ('b', 'd'), ('c', 'e'), ('d', 'a'), ('d', 'e'), ('f', 'c'), ('f', 'e')]
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']

    # CLI input syntax (optional): 
    # nodes="<node_name>: <neighboor_1> <neighboor_2> ..., <node_name>: ..."
    # Each node and its neighboors are comma separated, and each neighboor is space separated
    # Works with nodes with no neighboors and so no ":" as well. 
    # example: nodes="a: b c d, b: a d e, c, d: a e, e: a d, f: c e"
    for arg in sys.argv:
        if arg.startswith("nodes="):
            splitOnComma = arg.split("=")[1].replace("\"", "").split(", ")
            newEdges = []
            newVerts = []
            for nodeNeighboorPair in splitOnComma:
                if ":" in nodeNeighboorPair:
                    nodeNeighboorSplit = nodeNeighboorPair.split(": ")
                    node = nodeNeighboorSplit[0]
                    neighbors = nodeNeighboorSplit[1]
                    newVerts.append(node)
                    if neighbors is not None:
                        for neighbor in neighbors.strip().split(" "):
                            newEdges.append((node, neighbor))
                else:           
                    newVerts.append(nodeNeighboorPair)

            edges = newEdges
            vertices = newVerts

    print("All Topological sorts")
    # create a graph from edges
    graph = Graph(vertices)
    # add edges to the graph
    for edge in edges:
        graph.addEdge(edge[0], edge[1])
    # print all topological orderings of the graph
    printAllTopologicalOrders(graph)
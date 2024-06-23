from __future__ import annotations
from collections import OrderedDict

time = 0
treeEdges = []
backEdges = []
forwardEdges = []
crossEdges = []

# return discovery and fishing time for each vertex without having the cost of each edge
class Vertex:
    id: str = None
    connectedTo: dict[str, Vertex] = {}
    color: str = None
    d: int = None
    pi: Vertex | None = None
    f: float = None

    def __init__(self, key):
        self.id = key
        self.connectedTo: dict[str, Vertex] = {}
        self.color = "white"
        self.d = 0
        self.f = float("inf")
        self.pi = None

    def getNeighbors(self) -> dict[str, Vertex]:
        self.connectedTo = OrderedDict(sorted(self.connectedTo.items()))
        return self.connectedTo

    def addNeighbor(self, nbr: Vertex) -> None:
        self.connectedTo[nbr.id] = nbr

    def __str__(self) -> str:
        return str(self.id) + ' connectedTo: ' + str([x for x in self.connectedTo])

    def __repr__(self) -> str:
        return self.__str__()


def add_neighbours(dict_in: dict[Vertex, list[Vertex]], sort_alphabetically: bool = True) -> None:
    for vertex, neighbours in dict_in.items():
        sorted_neighbours = sorted(neighbours, key=lambda x: x.id) if sort_alphabetically else neighbours
        for neighbour in sorted_neighbours:
            vertex.addNeighbor(neighbour)


def DFS_Visit(G: list[Vertex], u: Vertex) -> None:
    global time

    time = time + 1
    u.d = time
    u.color = "gray"
    for v in u.getNeighbors().values():
        if v.color == "white":
            v.pi = u
            DFS_Visit(G, v)

    u.color = "black"
    time = time + 1
    u.f = time


def DFS(G: list[Vertex]) -> None:
    global time

    for u in G:
        u.color = "white"
        u.pi = None
    time = 0
    for u in G:
        if u.color == "white":
            DFS_Visit(G, u)


def edge_check(G: list[Vertex]) -> None:
    global time

    for u in G:
        for v in u.getNeighbors().values():
            if v.pi == u:  # Note that tree edges are the edges that are explored by the parent
                treeEdges.append((u.id, v.id))

            # elif are needed to avoid double counting since we no longer have the time variable to help us
            elif v.d <= u.d < u.f <= v.f:
                backEdges.append((u.id, v.id))

            elif u.d < v.d < v.f < u.f:
                forwardEdges.append((u.id, v.id))

            elif v.d < v.f < u.d < u.f:
                crossEdges.append((u.id, v.id))

            else:
                print(f"Error on edge: ('{u.id}',  '{v}')")


def get_vertex_by_time_order(G: list[Vertex]) -> list[Vertex]:
    return sorted(G, key=lambda x: x.d, reverse=False)

def get_vertex_by_finish_time_order(G: list[Vertex]) -> list[Vertex]:
    return sorted(G, key=lambda x: x.f, reverse=False)

import sys
def main():
    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    h = Vertex('h')
    vertList = {a, b, c, d, e, f, g, h}
    neighbourDict = {
        a: [b, e],
        b: [c, f],
        c: [g, f],
        d: [h],
        e: [],
        f: [e, a, g],
        g: [d],
        h: [g]
    }
    sortAlphabetically = False
    startNode = None

    # CLI input syntax (optional): 
    # nodes="<node_name>: <neighboor_1> <neighboor_2> ..., <node_name>: ..."
    # Each node and its neighboors are comma separated, and each neighboor is space separated
    # Works with nodes with no neighboors and so no ":" as well. 
    # example: nodes="a: b c d, b: a d e, c, d: a e, e: a d, f: c e"
    vertsFromStrs: dict[str, Vertex] = dict()
    newVerts: list[Vertex] = []
    newNeighbourDict: dict[Vertex, list[Vertex]] = dict()
    for arg in sys.argv:
        if arg.startswith("start="):
            startNode = arg.split("=")[1]
            if startNode not in vertsFromStrs:
                vertsFromStrs[startNode] = Vertex(startNode)
                newVerts.append(vertsFromStrs[startNode])

            if vertsFromStrs[startNode] not in newNeighbourDict:
                newNeighbourDict[vertsFromStrs[startNode]] = []
            
            startNode = vertsFromStrs[startNode]

        elif arg == "--alphabetical":
            sortAlphabetically = True

        elif arg.startswith("nodes="):
            splitOnComma = arg.split("=")[1].replace("\"", "").split(", ")
            for nodeNeighboorPair in splitOnComma:
                if ":" in nodeNeighboorPair:
                    nodeNeighboorSplit = nodeNeighboorPair.split(": ")
                    node = nodeNeighboorSplit[0]
                    neighbors = nodeNeighboorSplit[1].split()
                    if node not in vertsFromStrs:
                        vertsFromStrs[node] = Vertex(node)
                        newVerts.append(vertsFromStrs[node])
                    if vertsFromStrs[node] not in newNeighbourDict:
                        newNeighbourDict[vertsFromStrs[node]] = []
                    for neighbor in neighbors:
                        if neighbor not in vertsFromStrs:
                            vertsFromStrs[neighbor] = Vertex(neighbor)
                            newVerts.append(vertsFromStrs[neighbor])
                        newNeighbourDict[vertsFromStrs[node]].append(vertsFromStrs[neighbor])
                else:
                    node = nodeNeighboorPair
                    if node not in vertsFromStrs:
                        vertsFromStrs[node] = Vertex(node)
                        newVerts.append(vertsFromStrs[node])

    neighbourDict = newNeighbourDict
    vertList = newVerts

    add_neighbours(neighbourDict, sortAlphabetically)

    if startNode is None:
        print("Executing DFS")
        DFS(vertList)
    else:
        print("Executing DFS_Visit")
        DFS_Visit(vertList, startNode)
    edge_check(vertList)

    print("Tree Edges (" + str(len(treeEdges)) + "): ", treeEdges)
    print("Back Edges (" + str(len(backEdges)) + "): ", backEdges)
    print("Forward Edges (" + str(len(forwardEdges)) + "): ", forwardEdges)
    print("Cross Edges (" + str(len(crossEdges)) + "): ", crossEdges)

    for u in get_vertex_by_time_order(vertList):
        print(str(u.id) + " push: " + str(u.d) + " pop: " + str(u.f))


if (__name__ == "__main__"):
    main()
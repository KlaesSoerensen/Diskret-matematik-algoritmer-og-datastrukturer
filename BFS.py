from collections import OrderedDict

vertexAdded = []
vertexAddedStr = ""


class Vertex:
    id = None
    connectedTo = {}
    color = None
    d = None
    pi = None

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.d = 0
        self.pi = None

    def getNeighbors(self):
        self.connectedTo = OrderedDict(sorted(self.connectedTo.items()))
        return self.connectedTo

    def addNeighbor(self, nbr):
        self.connectedTo[nbr.id] = nbr

    def __str__(self):
        return str(self.id) + " " + self.color + " d=" + str(self.d)


def add_neighbours(dict, sort_alphabetically = False):
    for vertex, neighbours in dict.items():
        for neighbour in neighbours:
            vertex.addNeighbor(neighbour)


def BFS(G, s):
    for u in G:
        u.color = "white"
        u.d = float("inf")
        u.pi = None
    s.color = "gray"
    s.d = 0
    s.pi = None
    Q = []
    enqueue(Q, s)
    while Q != []:
        u = dequeue(G, Q)
        if u == None:
            return

        for v in u.getNeighbors().values():
            # print("Current Vertex: ", v.id)
            if v.color == "white":
                v.color = "gray"
                v.d = u.d + 1
                v.pi = u
                enqueue(Q, v)
        u.color = "black"


def enqueue(Q, u: Vertex):
    # print("Vertex to be added: ", u)
    addVertexToAddedList(u)
    if (u.id not in vertexAdded):
        Q.append(u.id)


def dequeue(G, Q):
    key = Q.pop(0)
    for i in range(len(G)):
        if G[i].id == key:
            # print("Vertex to be removed: ", G[i].id)
            return G[i]

    return None


def addVertexToAddedList(vertex: Vertex):
    global vertexAddedStr
    if (vertex not in vertexAdded):
        vertexAdded.append(vertex)
        vertexAddedStr += vertex.id
        # print("Vertex added: ", vertex.id)


def main():

    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    h = Vertex('h')
    i = Vertex('i')
    j = Vertex('j')
    vertList = {a, b, c, d, e, f, g, h}
    neighbourDict = {
       a:[e],
       b:[c],
       c:[f,h],
       d:[a,i,j],
       e:[b,d,g],
       f:[g],
       g:[c],
       h:[b],
       i:[j],
       j:[g]
    }
    startNode = None

    import sys
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

    if len(newNeighbourDict) > 0:
        neighbourDict = newNeighbourDict
    if len(newVerts) > 0:
        vertList = newVerts

    add_neighbours(neighbourDict)
    BFS(vertList, startNode)

    print("Vertex Added order: ")
    for vertex in vertList:
        print(str(vertex))


if (__name__ == "__main__"):
    main()
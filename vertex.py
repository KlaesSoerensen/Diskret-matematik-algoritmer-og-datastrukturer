from collections import OrderedDict
""" find disocvery and finish time of each vertex in a graph using DFS. Find also cross, forward and back edges """
time = 0
treeEdges = []
backEdges = []
forwardEdges = []
crossEdges = []


class Vertex:
    id = None
    connectedTo = {}
    color = None
    d = None
    pi = None
    f = None

    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.d = 0
        self.f = float("inf")
        self.pi = None

    def getNeighbors(self):
        # self.connectedTo = OrderedDict(sorted(self.connectedTo.items()))
        return self.connectedTo

    def addNeighbor(self, nbr):
        self.connectedTo[nbr.id] = nbr

    def __str__(self):
        return str(self.id) + ' connectedTo: ' + str([x for x in self.connectedTo])

    def __repr__(self) -> str:
        return self.__str__()


def add_neighbours(dict):
    for vertex, neighbours in dict.items():
        for neighbour in neighbours:
            vertex.addNeighbor(neighbour)


def DFS_Visit(G, u):
    global time

    time = time + 1
    u.d = time
    u.color = "gray"
    for v in u.getNeighbors().values():
        if (
            v.color == "white"
        ):
            treeEdges.append((u.id, v.id))
        if (
            v.color == "gray"
            and v.d <= u.d <= time < u.f <= v.f
        ):
            backEdges.append((u.id, v.id))
        if (
            v.color == "black"
            and u.d < v.d < v.f < time < u.f
        ):
            forwardEdges.append((u.id, v.id))
        if (
            v.color == "black"
            and v.d < v.f < u.d <= time < u.f
        ):
            crossEdges.append((u.id, v.id))

        if v.color == "white":
            v.pi = u
            DFS_Visit(G, v)

            

    u.color = "black"
    time = time + 1
    u.f = time

    """ 
    if v.color == "white":
    v.pi = u
    treeEdges.append((u.id, v.id))
    DFS_Visit(G, v)
elif v.color == "gray":
    backEdges.append((u.id, v.id))
elif v.color == "black":
    if u.d < v.d < v.f < u.f:
        forwardEdges.append((u.id, v.id))
    elif u.d < v.f < u.f:
        crossEdges.append((u.id, v.id))
      """


def DFS(G):
    global time

    for u in G:
        u.color = "white"
        u.pi = None
    time = 0
    for u in G:
        if u.color == "white":
            DFS_Visit(G, u)


def get_vertex_by_time_order(G):
    global time

    vertexs = []

    for i in range(time):
        for u in G:
            if (u.d == i):
                vertexs.append(u)
    return vertexs


def main():

    # a = Vertex('a')
    # b = Vertex('b')
    # c = Vertex('c')
    # d = Vertex('d')
    # e = Vertex('e')
    # f = Vertex('f')
    # g = Vertex('g')
    # h = Vertex('h')
    # i = Vertex('i')

    # add_neighbours({
    #     e: [d, a],
    #     d: [e, g],
    #     h: [d, g, f],
    #     a: [d, g],
    #     g: [h, i, b],
    #     f: [g, b],
    #     i: [a, b],
    #     b: [c],
    #     c: [b, f]
    # })
    #
    # Vertexs = [a, b, c, d, e, f, g, h, i]

    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    h = Vertex('h')
    i = Vertex('i')

    Vertexs = [a, b, c, d, e, f, g, h,i]

    add_neighbours({
        a: [d,b],
        b: [c, d],
        c: [e],
        d: [e],
        e: [g,f, b],
        f: [h, i,c],
        g: [d, h],
        h: [e],
        i: []
    })

    DFS(Vertexs)

    print("Tree Edges (" + str(len(treeEdges)) + "): ", treeEdges)
    print("Back Edges (" + str(len(backEdges)) + "): ", backEdges)
    print("Forward Edges (" + str(len(forwardEdges)) + "): ", forwardEdges)
    print("Cross Edges (" + str(len(crossEdges)) + "): ", crossEdges)

    for u in get_vertex_by_time_order(Vertexs):
        print(u.id, u.d, u.f)


if (__name__ == "__main__"):
    main()
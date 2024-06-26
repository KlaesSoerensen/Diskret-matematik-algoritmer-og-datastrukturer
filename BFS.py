from collections import OrderedDict

vertexAdded = []
vertexAddedStr = ""
action_steps = []


class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectedTo = {}
        self.color = "white"
        self.d = float("inf")
        self.pi = None

    def getNeighbors(self):
        self.connectedTo = OrderedDict(sorted(self.connectedTo.items()))
        return self.connectedTo

    def addNeighbor(self, nbr):
        self.connectedTo[nbr.id] = nbr

    def __str__(self):
        return str(self.id) + " " + self.color + " d=" + ("inf" if self.d == float("inf") else str(self.d))


def add_neighbours(neighbour_dict):
    for vertex, neighbours in neighbour_dict.items():
        for neighbour in neighbours:
            vertex.addNeighbor(neighbour)


def BFS(G, s):
    order = []
    push_pop_log = []
    step = 1
    for u in G:
        u.color = "white"
        u.d = float("inf")
        u.pi = None
    s.color = "gray"
    s.d = 0
    s.pi = None
    Q = []
    enqueue(Q, s, push_pop_log, step)
    step += 1
    while Q != []:
        u = dequeue(G, Q, push_pop_log, step)
        step += 1
        if u is None:
            return None

        order.append(u)
        for v in u.getNeighbors().values():
            if v.color == "white":
                v.color = "gray"
                v.d = u.d + 1
                v.pi = u
                enqueue(Q, v, push_pop_log, step)
                step += 1
        u.color = "black"
    return order, push_pop_log


def enqueue(Q, u: Vertex, log, step):
    addVertexToAddedList(u)
    if u.id not in vertexAdded:
        Q.append(u.id)
        log.append({"step": step, "action": "Push", "vertex": u.id})


def dequeue(G, Q, log, step):
    key = Q.pop(0)
    log.append({"step": step, "action": "Pop", "vertex": key})
    for i in range(len(G)):
        if G[i].id == key:
            return G[i]
    return None


def addVertexToAddedList(vertex: Vertex):
    global vertexAddedStr
    if vertex not in vertexAdded:
        vertexAdded.append(vertex)
        vertexAddedStr += vertex.id


def main():
    import sys
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
    vertList = [a, b, c, d, e, f, g, h]
    neighbourDict = {
        a: [e],
        b: [c],
        c: [f, h],
        d: [a, i, j],
        e: [b, d, g],
        f: [g],
        g: [c],
        h: [b],
        i: [j],
        j: [g]
    }
    startNode = None

    vertsFromStrs = {}
    newVerts = []
    newNeighbourDict = {}
    for arg in sys.argv:
        if arg.startswith("start="):
            startNodeKey = arg.split("=")[1]
            if startNodeKey not in vertsFromStrs:
                vertsFromStrs[startNodeKey] = Vertex(startNodeKey)
                newVerts.append(vertsFromStrs[startNodeKey])
            startNode = vertsFromStrs[startNodeKey]

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
        vertList = list(newVerts)

    add_neighbours(neighbourDict)

    if startNode is None:
        print("Start node is not defined.")
        return

    order, push_pop_log = BFS(vertList, startNode)

    if order is None:
        print("BFS did not return a valid order.")
        return

    print("Order of vertices visited:")
    for vertex in vertList:
        print(str(vertex))

    print("\nQueue operations (push/pop):")
    for log_entry in push_pop_log:
        print(f"Step {log_entry['step']}: {log_entry['action']} {log_entry['vertex']}")


if __name__ == "__main__":
    main()

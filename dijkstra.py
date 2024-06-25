import sys


class Graph:
    # Find the shortest path from the start node to all other nodes
    # return how many times the relax operation was used in each kante
    def __init__(self):
        self.vertices: dict[str, dict[str, int]] = {}

    def add_vertex(self, vertex: str) -> None:
        self.vertices[vertex] = {}

    def add_edge(self, start_vertex: str, end_vertex: str, cost: int) -> None:
        self.vertices[start_vertex][end_vertex] = cost

    def get_neighbors(self, vertex: str) -> dict[str, int]:
        return self.vertices[vertex]

    def dijkstra(self, start_vertex: str, actionLimit: int = -1, verbose: bool = False):
        distances: dict[str, int] = {v: sys.maxsize for v in self.vertices}
        distances[start_vertex] = 0
        visited = set()

        previous: dict[str, str] = {v: None for v in self.vertices}
        changed_edges: list[tuple[str, str]] = []
        visited_order: list[str] = []
        push_order = set()
        push_tracker = 0
        pop_tracker = 0

        queue = [(start_vertex, 0)]
        while len(queue) > 0:
            queue = sorted(queue, key=lambda x: distances[x[0]])
            current_vertex, current_distance = queue[0]
            queue.remove((current_vertex, current_distance))
            pop_tracker += 1
            if verbose:
                print(f"Pop {pop_tracker} node: {current_vertex} action #: {push_tracker + pop_tracker}")

            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            visited_order.append(current_vertex)

            if actionLimit != -1 and (push_tracker + pop_tracker) >= actionLimit:
                break

            for neighbor, cost_along_edge in self.get_neighbors(current_vertex).items():
                if current_distance + cost_along_edge < distances[neighbor]:
                    distances[neighbor] = current_distance + cost_along_edge
                    previous[neighbor] = current_vertex
                    changed_edges.append((current_vertex, neighbor))

                queue.append((neighbor, distances[neighbor]))
                push_tracker += 1
                if verbose:
                    print(f"Push {push_tracker} vertex: {neighbor} action #: {push_tracker + pop_tracker}")
                push_order.add(neighbor)

            if actionLimit != -1 and (push_tracker + pop_tracker) >= actionLimit:
                break

        return distances, previous, changed_edges, visited_order, push_order


def print_path_to_node(to: str, starting_at: str, previous_ordering: dict[str, str]):
    step = to
    backtrack = list(step)
    while step != starting_at and step is not None:
        step = previous_ordering[step]
        backtrack.append(step)

    print(list(reversed(backtrack)))

def print_all_paths(starting_at: str, graph: Graph, previous_ordering: dict[str, str]):
    for vertex in graph.vertices:
        print_path_to_node(vertex, starting_at, previous_ordering)

def printAll(graph: Graph, start_vertex: str, actionLimit: int = -1, verbose: bool = False):
    distances, previous, changed_edges, visited_order, push_order = graph.dijkstra(start_vertex, actionLimit, verbose)

    print("Shortest distances from vertex", start_vertex + ":")
    for vertex, distance in distances.items():
        print(vertex, "-", distance)

    print("\nPrevious nodes:")
    for vertex, prev in previous.items():
        print(vertex, "-", prev)

    print("\nall paths:")
    print_all_paths(start_vertex, graph, previous)

    print("\nEdges changed by RELAX method:")
    for edge in changed_edges:
        print(edge[0], "->", edge[1])
    print(f"Total edges changed by RELAX: {len(changed_edges)}")

    print("\nVisited order (pop):")
    print(visited_order)

    print("\nPush order:")
    print(push_order)

def emanuel():
    # Example usage:
    graph = Graph()
    # Add vertexes
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_vertex('C')
    graph.add_vertex('D')
    graph.add_vertex('E')
    graph.add_vertex('F')
    graph.add_vertex('G')
    # Add edges with cost values
    graph.add_edge('A', 'B', 4)
    graph.add_edge('A', 'G', 7)

    graph.add_edge('B', 'C', 1)
    graph.add_edge('B', 'D', 2)

    graph.add_edge('C', 'A', 2)
    graph.add_edge('C', 'F', 6)

    graph.add_edge('D', 'C', 1)
    graph.add_edge('D', 'F', 4)

    graph.add_edge('E', 'C', 8)

    graph.add_edge('F', 'E', 1)

    graph.add_edge('G', 'E', 6)
    graph.add_edge('G', 'C', 4)

    start_vertex = 'A'
    printAll(graph, start_vertex)

import sys
def fromCLIInput(args: list[str]):
    graph = Graph()
    start_vertex = None
    actionLimit = -1
    verbose = False

    for arg in args:
        if arg.startswith("--verbose"): # Optional flag, if present, print all actions when taken
            verbose = True
        if arg.startswith("actionLimit="): # Optional limit, if present, limit the amount of actions taken before the algorithm stops
            actionLimit = int(arg.split("=")[1].strip())
        if arg.startswith("start="): # Required for CLI input, the starting vertex
            start_vertex = arg.split("=")[1].strip()
        if arg.startswith("nodes="): # Required for CLI input, the nodes and their neighboors
            splitOnComma = arg.split("=")[1].replace("\"", "").split(", ")
            for nodeNeighboorPair in splitOnComma:
                if ":" in nodeNeighboorPair:
                    nodeNeighboorSplit = nodeNeighboorPair.split(": ")
                    node = nodeNeighboorSplit[0].strip()
                    graph.add_vertex(node)
                    neighbors = nodeNeighboorSplit[1].strip()
                    if neighbors is not None:
                        neighboorSplit = neighbors.split(" ")
                        # For each 2 elements, first is node name, second is cost
                        # in mem: neighboorSplit = [a, 3, b, 4, c, 2]
                        for i in range(0, len(neighboorSplit), 2):
                            graph.add_edge(node, neighboorSplit[i], int(neighboorSplit[i + 1]))
    
                else:
                    graph.add_vertex(nodeNeighboorPair)

    printAll(graph, start_vertex, actionLimit=actionLimit, verbose=verbose)
    

if __name__ == '__main__':

    # start=a
    # nodes="a, b: g 1 k 4, c: a_2 b_4 c_2"

    # CLI input syntax (optional): 
	# nodes="<node_name>: <neighboor_1> <cost_1> <neighboor_2> <cost_2> ..., <node_name>: ..."
    # start="<node_name>"

	# Each node and its neighboors are comma separated, and each neighboor is space separated
	# Works with nodes with no neighboors and so no ":" as well. 
	# example: nodes="a: b 1 c 4 d 2, c, d: a 8 e 1, e"

    for arg in sys.argv:
        if arg.startswith("start=") or arg.startswith("nodes="):
            fromCLIInput(sys.argv)
            exit(0)

    emanuel()
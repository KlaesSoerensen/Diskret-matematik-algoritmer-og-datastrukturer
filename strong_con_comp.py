from dataclasses import dataclass, field

@dataclass
class Vertex:
	""" Find all strongly connected components in a graph without having costs on the edges. """
	name: str = field(hash=True)
	neighbors: set['Vertex'] = field(default_factory=set) # default = []

	def __str__(self):
		return self.name

	def __repr__(self) -> str:
		return self.__str__()

	def __eq__(self, o: object) -> bool:
		return isinstance(o, Vertex) and self.name == o.name

	def __hash__(self) -> int:
		return hash(self.name)

def get_all_connected_vertices(vertex: Vertex, connected_vertices: set | None = None) -> set[Vertex]:
	if connected_vertices is None:
		connected_vertices = set()
	connected_vertices.add(vertex)
	for neighbor in vertex.neighbors:
		if neighbor not in connected_vertices:
			connected_vertices |= get_all_connected_vertices(neighbor, connected_vertices)
	return connected_vertices

# get all vertices reachable from vertex
def get_connections(graph: set[Vertex]) -> dict[Vertex, set[Vertex]]:
	connections = {}
	for vertex in graph:
		connections[vertex] = get_all_connected_vertices(vertex)
	return connections

# get all strongly connected components in graph
def get_strongly_connected_components(graph: set[Vertex]) -> list[set[Vertex]]:
	connections = get_connections(graph)

	components = []
	for vertex in graph:
		component = {vertex}
		for other_vertex in graph:
			if vertex is other_vertex:
				continue

			if vertex in connections[other_vertex] and other_vertex in connections[vertex]:
				component.add(other_vertex)
		components.append(component)
	# remove duplicates
	components = [component for i, component in enumerate(components) if component not in components[:i]]
	return components

import sys
# Driver code
if __name__ == '__main__':
	# List of graph edges as per above diagram
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

	a.neighbors = {b}
	b.neighbors = {f,c}
	c.neighbors = {d}
	d.neighbors = {e}
	e.neighbors = {c}
	f.neighbors = {i,e}
	g.neighbors = {f}
	h.neighbors = {j}
	i.neighbors = {e}
	j.neighbors = {b,g}

	graph = {a, b, c, d, e, f, g, h, i, j}

	# CLI input syntax (optional): 
	# nodes="<node_name>: <neighboor_1> <neighboor_2> ..., <node_name>: ..."
	# Each node and its neighboors are comma separated, and each neighboor is space separated
	# Works with nodes with no neighboors and so no ":" as well. 
	# example: nodes="a: b c d, b: a d e, c, d: a e, e: a d, f: c e"
	for arg in sys.argv:
		if arg.startswith("nodes="):
			splitOnComma = arg.split("=")[1].replace("\"", "").split(", ")
			newGraph = set()
			vertices = {}
			for nodeNeighboorPair in splitOnComma:
				if ":" in nodeNeighboorPair:
					nodeNeighboorSplit = nodeNeighboorPair.split(": ")
					node = nodeNeighboorSplit[0]
					vertices[node] = Vertex(node)
					neighbors = nodeNeighboorSplit[1]
					if neighbors is not None:
						for neighbor in neighbors.strip().split(" "):
							if neighbor not in vertices:
								vertices[neighbor] = Vertex(neighbor)
							vertices[node].neighbors.add(vertices[neighbor])	
					newGraph.add(vertices[node])
				else:
					vertices[nodeNeighboorPair] = Vertex(nodeNeighboorPair)
					newGraph.add(vertices[nodeNeighboorPair])

			graph = newGraph

	components = get_strongly_connected_components(graph)

	print('strongly connected components:')
	for component in components:
		print(component)
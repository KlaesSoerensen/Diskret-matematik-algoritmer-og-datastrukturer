from dataclasses import dataclass, field
from typing import Self

@dataclass
class Vertex:
	name: str
	neighbors: list[Self | None] = field(default_factory=list) # default = []

	def __str__(self):
		return self.name

	def __repr__(self) -> str:
		return self.__str__()


def is_topological_sorting(vertices: list[Vertex]) -> bool:
	for i in range(1, len(vertices)):
		vertex = vertices[i]
		for neighbor in vertex.neighbors:
			if neighbor in vertices[:i]:
				return False
	return True

if (__name__ == "__main__"):
	a = Vertex('a')
	b = Vertex('b')
	c = Vertex('c')
	d = Vertex('d')
	e = Vertex('e')
	f = Vertex('f')
	g = Vertex('g')

	a.neighbors = [b,d]
	b.neighbors = [d, e]
	c.neighbors = [f]
	d.neighbors = []
	e.neighbors = [d,f]
	f.neighbors = []
	g.neighbors = [c,f]

	sortings = [
		[a, b, c, d, e, f,g],
		[a,b, e, d,c, g, f],
		[a,b,e,d,g,c,f],
		[a,b,g,c,e,d,f],
		[g,a,b,e,c,f,d]
	]

	for sorting in sortings:
		print(f'is_topological_sorting({sorting}) = {is_topological_sorting(sorting)}')
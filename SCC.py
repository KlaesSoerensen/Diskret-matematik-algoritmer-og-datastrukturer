# Kosaraju's algorithm to find strongly connected components in Python


from collections import defaultdict

class Graph:

    def __init__(self, vertex):
        self.V = vertex
        self.graph = defaultdict(list)

    # Add edge into the graph
    def add_edge(self, s, d):
        self.graph[s].append(d)

    # dfs
    def dfs(self, d, visited_vertex):
        visited_vertex[d] = True
        print(d, end='')
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.dfs(i, visited_vertex)

    def fill_order(self, d, visited_vertex, stack):
        visited_vertex[d] = True
        for i in self.graph[d]:
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)
        stack = stack.append(d)

    # transpose the matrix
    def transpose(self):
        g = Graph(self.V)

        for i in self.graph:
            for j in self.graph[i]:
                g.add_edge(j, i)
        return g

    # Print stongly connected components
    def print_scc(self):
        stack = []
        visited_vertex = [False] * (self.V)

        for i in range(self.V):
            if not visited_vertex[i]:
                self.fill_order(i, visited_vertex, stack)

        gr = self.transpose()

        visited_vertex = [False] * (self.V)

        while stack:
            i = stack.pop()
            if not visited_vertex[i]:
                gr.dfs(i, visited_vertex)
                print("")

letters = {
    'a': 1,
    'b': 2,
    'c': 3,
    'd': 4,
    'e': 5,
    'f':6,
    'g':7,
    'h':8,
    'i':9,
}
g = Graph(10)
g.add_edge(letters['c'],letters['g'])
g.add_edge(letters['c'],letters['d'])
g.add_edge(letters['d'],letters['h'])
g.add_edge(letters['h'],letters['c'])
g.add_edge(letters['c'],letters['g'])
g.add_edge(letters['g'],letters['f'])
g.add_edge(letters['g'],letters['b'])
g.add_edge(letters['b'],letters['f'])
g.add_edge(letters['b'],letters['a'])
g.add_edge(letters['f'],letters['a'])


if __name__ == "__main__":
    print("Nodes are numbered from 0..n"
          "\nThis means if the nodes are lettered:"
          "\na=0"
          "\nb=1"
          "\nc=2"
          "\netc..")
    """ node_amount = int(input("Enter amount of nodes:\n"))
    g = Graph(node_amount) """

    """ print("Enter edges separated by comma:"
          "\nType exit or 0 to exit")
    while True:
        user_input = input("Edge separated by comma:\n").strip() or "0"
        if user_input == "exit" or user_input == "0":
            break
        edge = [int(item) for item in user_input.split(",")]
        g.add_edge(edge[0], edge[1]) """

    print("Strongly Connected Components:")
    g.print_scc()
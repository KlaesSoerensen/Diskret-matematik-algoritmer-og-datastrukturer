from collections import defaultdict, deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        node = queue.popleft()
        print(node, end=" ")  # Modify this line as per your requirement

        for neighbor in graph[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True


def kosaraju_bfs(graph):
    # Step 1: Perform a normal BFS to determine the order of traversal
    num_vertices = len(graph)
    visited = [False] * num_vertices
    traversal_order = deque()

    for vertex in range(num_vertices):
        if not visited[vertex]:
            bfs(graph, vertex, visited)
            traversal_order.appendleft(vertex)

    # Step 2: Reverse the graph
    reversed_graph = defaultdict(list)
    for vertex in graph:
        for neighbor in graph[vertex]:
            reversed_graph[neighbor].append(vertex)

    # Step 3: Perform BFS on the reversed graph in the order obtained from Step 1
    visited = [False] * num_vertices

    while traversal_order:
        vertex = traversal_order.popleft()
        if not visited[vertex]:
            bfs(reversed_graph, vertex, visited)
            print()  # Add a newline for each strongly connected component


letters = {
    'a': 0,
    'b': 1,
    'c': 2,
    'd': 3,
    'e': 4,
    'f': 5,
    'g': 6,
    'h': 7,
    'i': 8
}

# Example usage
graph = {
    letters['c']: [letters['b'], letters['g'], letters['d']],
    letters['a']: [letters['b']],
    letters['b']: [letters['g'], letters['f']],
    letters['d']: [letters['h']],
    letters['e']: [letters['d'], letters['i']],
    letters['f']: [letters['a'], letters['g']],
    letters['g']: [],
    letters['h']: [letters['c'], letters['i']],
    letters['i']: [letters['d']]
}

print("Strongly Connected Components:")
kosaraju_bfs(graph)

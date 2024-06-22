import networkx as nx

relations = [('a', 'b'), ('a', 'c'), ('b', 'b'), ('c', 'd'), ('d', 'e')]

import sys
#Input syntax: range="a b, c d, e f, ..."
for arg in sys.argv:
    if arg.startswith("range="):
        splitOnComma = arg.split("=")[1].replace("\"", "").split(",")
        tempRange = []
        for pair in splitOnComma:
            splitOnSpace = pair.strip().split(" ")
            a = splitOnSpace[0]
            b = splitOnSpace[1]
            tempRange.append((a, b))

        relations = tempRange
        

# Opret en rettet graf
G = nx.DiGraph()

# Tilføj relationerne som kanter i grafen
G.add_edges_from(relations)

# Find den transitive lukning
transitive_closure = nx.transitive_closure(G)

# Udskriv de transitive relationer
output = list(transitive_closure.edges())
print(output)

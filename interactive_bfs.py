from collections import OrderedDict

queue = list(input('enter start-node: '))

visited_nodes = [
        ("a","b"),
        ("b","f"),
        ("b","g"),
        ("c","b"),
        ("c","g"),
        ("c","d"),
        ("d","h"),
        ("e","d"),
        ("e","i"),
        ("f","a"),
        ("f","g"),
        ("h","c"),
        ("h","i"),
        ("i","d"),


]

while queue:
    visited_nodes.append(queue.pop(0))
    print(f'{visited_nodes = }')
    print(f'{queue = }')
    adjacent_nodes = input(f'Please enter the nodes adjacent to {visited_nodes[-1]}: ')
    adjacent_nodes = sorted(list(adjacent_nodes.lower()))
    queue.extend([n for n in adjacent_nodes if n not in visited_nodes])
    queue = list(OrderedDict.fromkeys(queue))

print(visited_nodes)
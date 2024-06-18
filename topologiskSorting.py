from DFS import Vertex, get_vertex_by_finish_time_order, get_vertex_by_time_order, add_neighbours, DFS

time = 0


def Topologisk_sorting(G):
    DFS(G)
    ordered_list = get_vertex_by_finish_time_order(G)
    ordered_list.reverse()
    return ordered_list


def main():

    a = Vertex('a')
    b = Vertex('b')
    c = Vertex('c')
    d = Vertex('d')
    e = Vertex('e')
    f = Vertex('f')
    g = Vertex('g')
    

    add_neighbours({
        a: [b,d],
        b: [d, e],
        c: [f],
        d: [],
        e: [d,f],
        f: [],
        g: [c,f]
    })

    Vertexs = [
        g,f,b,c,d,a,e
    ]

    DFS(Vertexs)

    for u in Topologisk_sorting(Vertexs):
        print(u.id)


if (__name__ == "__main__"):
    main()
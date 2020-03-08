import pprint
import argparse

def create_graph(n):
    graph = {}
    for x in range(-(n - 2), n):
        if x < 0:
            k = 1
        else:
            k = 0
        for y in range(k, n - abs(x)):
            loc = []
            if x < 0:
                loc.append((x + 1, y))
                if abs(x) + y + 1 < n:
                    loc.append((x, y + 1))
                    loc.append((x - 1, y))
                if y - 1 >= 1:
                    loc.append((x, y - 1))
            else:
                if x + y + 1 < n:
                    loc.append((x + 1, y))
                    loc.append((x, y + 1))
                if not (x == 0 and (y == 0 or y == n - 1)):
                    loc.append((x - 1, y))
                if y - 1 >= 0:
                    loc.append((x, y - 1))
            graph[(x, y)] = loc
    return graph

def neighbors(G, p, v, u):
    for j in p:
        if j != u:
            if j in G:
                if v in G[j]:
                    return False
    return True

def CountFixedPolyominoes(G, untried, n, p, c):
    while not (len(untried) == 0):
        u = untried.pop()
        p.append(u)
        if len(p) == n:
            c[0] = c[0] + 1
        else:
            new_neighbors = set()
            for v in G[u]:
                if (v not in untried) and (v not in p) and neighbors(G, p, v, u):
                    new_neighbors.add(v)
            new_untried = untried.union(new_neighbors)
            CountFixedPolyominoes(G, new_untried, n, p, c)
        p.remove(u)
    return c[0]

parser = argparse.ArgumentParser()
parser.add_argument("size", type=int, help="display a number of free polyominoes with a specific size")
parser.add_argument("-p", help="print graph", action="store_true")
args = parser.parse_args()
n = args.size
graph = create_graph(n) 
if args.p:
    pprint.pprint(graph)
print(CountFixedPolyominoes(graph, {(0, 0)}, n, [], [0]))

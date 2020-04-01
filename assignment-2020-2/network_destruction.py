import argparse

def read_file(file):
    g = {}
    with open(file) as graph_input:
        for line in graph_input:
            nodes = [int(x) for x in line.split()]
            if len(nodes) != 2:
                continue
            if nodes[0] not in g:
                g[nodes[0]] = []
            if nodes[1] not in g:
                g[nodes[1]] = []
            g[nodes[0]].append(nodes[1])
            g[nodes[1]].append(nodes[0])
    return g

def degree_number_method(g, num_nodes):
    max = -1 
    for i in g:
        l = len(g[i])
        if l > max:
            max = l
            node_with_max_edges = i
    print(node_with_max_edges, max, sep=" ")
    if num_nodes != 1:
        for node in g[node_with_max_edges]:
            g[node].remove(node_with_max_edges)
        del g[node_with_max_edges]
        degree_number_method(g, num_nodes-1)

def ball(g, node, r):
    q = []
    distance_from_node = [-1 for i in range(0,len(g) + 1)]
    inqueue = [-1 for i in range(0,len(g) + 1)]
    q.append(node)
    inqueue[node] = 0
    while q:
        c = q[0]
        del q[0]
        distance_from_node[c] = inqueue[c]
        inqueue[c] = -1 
        if distance_from_node[c] == r:
            continue
        for v in g[c]:
            if (distance_from_node[v] == -1) and (inqueue[v] == -1):
                q.append(v)
                inqueue[v] = distance_from_node[c] + 1
    return distance_from_node

def th_ball(g, node, r):
    inside_ball = ball(g, node, r)
    return [i for i in range(0,len(inside_ball)) if inside_ball[i] == r]

def ball_list(g, node, r):
    inside_ball = ball(g, node, r)
    return [i for i in range(0,len(inside_ball)) if inside_ball[i] >= 0]

def influence_method(g, num_nodes, r):
    t_infl = {}
    max = -1
    for i in g:
        blist = th_ball(g, i, r)
        b = 0
        for j in blist:
            b += len(g[j]) - 1
        t_infl[i] = (len(g[i]) - 1) * b
        if max < t_infl[i]:
           max = t_infl[i]
           node_with_max_edges = i
    print (node_with_max_edges, max, sep=" ")
    for k in range(0, num_nodes-1):
        ball = ball_list(g, node_with_max_edges, r + 1)
        for node in g[node_with_max_edges]:
            g[node].remove(node_with_max_edges)
        g[node_with_max_edges] = []
        for i in ball:
            blist = th_ball(g, i, r)
            S = 0
            for j in blist:
                S += len(g[j]) - 1
            t_infl[i] = (len(g[i]) - 1) * S
        max = -1 
        for i in t_infl:
            if max < t_infl[i]:
                max = t_infl[i]
                node_with_max_edges = i
        print (node_with_max_edges, max, sep=" ")
    
parser = argparse.ArgumentParser()
parser.add_argument("-c", action="store_true", help="display nodes of the graph for deletion according to degree number method")
parser.add_argument("-r", "--radius", type=int, help="display nodes of the graph for deletion according to influence method")
parser.add_argument("num_nodes", type=int, help="the number of nodes we want to delete")
parser.add_argument("input_file", action='store', type=str, help="the file with the graph")
args = parser.parse_args()
g = read_file(args.input_file)
if args.c:
    degree_number_method(g, args.num_nodes)
if args.radius != None:
    influence_method(g, args.num_nodes, args.radius)

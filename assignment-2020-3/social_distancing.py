import math
import linkedlist
import random
import argparse

def read_file(file):
    space = []
    with open(file) as graph_input:
        for line in graph_input:
            nodes = [float(x) for x in line.split()]
            if len(nodes) != 4:
                continue
            space.append(((nodes[0],nodes[1]),(nodes[2],nodes[3])))
    return space

def tangent_circle(cm, rm, cn, rn, r):
    dx = cn[0] - cm[0]
    dy = cn[1] - cm[1]
    d = math.sqrt(dx**2 + dy**2)
    r1 = rm + r
    r2 = rn + r
    l = (r1**2 - r2**2 + d**2)/(2*d*d)
    e = math.sqrt((r1**2)/(d**2) - l**2)
    kx = cm[0] + l*dx - e*dy
    ky = cm[1] + l*dy + e*dx
    kx = round(kx, 2)
    ky = round(ky, 2)
    return (kx, ky)

def tangent_line(l, c):
    u = l[0]
    v = l[1]
    l2 = (u[0] - v[0])**2 + (u[1] - v[1])**2
    if l2 == 0:
        d = math.sqrt((u[0] - c[0])**2 + (u[1] - c[1])**2)
        return d
    t = ((c[0] - u[0])*(v[0] - u[0]) + (c[1] - u[1])*(v[1] - u[1]))/l2
    t = max(0, min(1,t))
    px = u[0] + t*(v[0] - u[0])
    py = u[1] + t*(v[1] - u[1])
    d = math.sqrt((px - c[0])**2 + ((py - c[1])**2))
    return round(d, 2)

def check_space_limits(space_list, c, r):
    for l in space_list:
        if tangent_line(l, c) < r:
            return True
    return False

def distance_from_start(center):
    return math.sqrt((center[0])**2 + (center[1])**2)

def add_in_graph(dist_from_start, dist, circle):
    if dist in dist_from_start:
        l = dist_from_start[dist]
        l.append(circle)
        return
    dist_from_start[dist] = [circle]

def find_min_dist(dist_from_start):
    dist = min(dist_from_start)
    m = dist_from_start[dist]
    m = m[0]
    return (m[0], m[1], dist)

def are_tangent_circles(c1, r1, c2, r2):
    dx = c1[0] - c2[0]
    dy = c1[1] - c2[1]
    d = math.sqrt(dx**2 + dy**2)
    if round(d, 2) < (r1 + r2):
        return True
    return False

def add_again(dist_from_start, l, listt):
    prev =  l.find_prev((listt[0])[0])
    #n = prev.next
    type = (listt[0])[1]
    for i in range(1, len(listt)):
        circle = (listt[-i])[0]
        l.add(prev, circle)
        index = (listt[-i])[1]
        dist = circle[2]
        if dist in dist_from_start:
            spec_dist = dist_from_start[dist]
            spec_dist.insert(index, (circle[0], circle[1]))
        else:
            dist_from_start[dist] = [(circle[0], circle[1])]
        if type == "pr":
            prev = prev.next
            #continue
        #n = n.prev

'''
def delete_front_nodes(listt, dist_from_start, node1, node2, type):
    deletad_nodes = []
    if type == "pr":
        flag = True
        middle = node1.prev
        deletad_nodes.append((node1.value, "pr"))
        while(flag):
            dist = middle.value[2]
            l = dist_from_start[dist]
            index = l.index((middle.value[0], middle.value[1]))
            del l[index]
            deletad_nodes.append((middle.value, index))
            if not l:
                del dist_from_start[dist]
            listt.remove(middle.prev, middle.next)
            middle = middle.prev
            if middle == node2:
                flag = False
        return deletad_nodes
    flag = True
    middle = node1.next
    deletad_nodes.append((node2.value, "next"))
    while(flag):
        dist = middle.value[2]        
        l = dist_from_start[dist]
        index = l.index((middle.value[0], middle.value[1]))
        del l[index]
        deletad_nodes.append((middle.value, index))
        if not l:
            del dist_from_start[dist]
        listt.remove(middle.prev, middle.next)
        middle = middle.next 
        if middle == node2:
            flag = False
    return deletad_nodes
'''

def delete_front_nodes(listt, dist_from_start, node1, node2, type):
    deleted_nodes = []
    if type == "pr":
        flag = True
        middle = node1.prev
        while(flag):
            dist = middle.value[2]
            l = dist_from_start.get(dist)
            if l == None:
                global cm_might_not_dead
                cm_might_not_dead.append(middle.value)
            else:    
                elem = (middle.value[0], middle.value[1])
                index = l.index(elem) if elem in l else -1
                if index != -1:
                    del l[index]
                    deleted_nodes.append((middle.value, index))
                    #l.remove((middle.value[0], middle.value[1]))
                    if not l:
                        del dist_from_start[dist]
                    #listt.remove(middle.prev, middle.next)
                else:
                    #global cm_might_not_dead
                    cm_might_not_dead.append(middle.value)
            listt.remove(middle.prev, middle.next)
            middle = middle.prev
            if middle == node2:
                flag = False
        return deleted_nodes
    flag = True
    middle = node1.next
    while(flag):
        dist = middle.value[2]        
        l = dist_from_start.get(dist)
        if l == None:
            cm_might_not_dead.append(middle.value)
        else:
            elem =(middle.value[0], middle.value[1])
            index = l.index(elem) if elem in l else -1
            if index != -1:
                del l[index]
                deleted_nodes.append((middle.value, index))
                #l.remove((middle.value[0], middle.value[1]))
                if not l:
                    del dist_from_start[dist]
                #listt.remove(middle.prev, middle.next)
            else:
                #global cm_might_not_dead
                cm_might_not_dead.append(middle.value)
        listt.remove(middle.prev, middle.next)
        #print("***************************")
        #listt.printLL()
        middle = middle.next 
        if middle == node2:
            flag = False
    return deleted_nodes

def circle_tangert_front(l, dist_from_start, pr, n, c, r):
    half_size = math.floor(l.size/2)
    nn = n
    mm = pr
    cn = n.value[0]
    rn = n.value[1]
    cm = pr.value[0]
    rm = pr.value[1]
    for i in range(half_size):
        pr = pr.prev
        c1 = pr.value[0]
        r1 = pr.value[1]
        if are_tangent_circles(c1 , r1, c, r):
            deleted = delete_front_nodes(l, dist_from_start, nn,  pr, "pr")
            return (nn, pr, deleted)
        n = n.next
        c1 = n.value[0]
        r1 = n.value[1]
        if are_tangent_circles(c1 , r1, c, r):
            deleted = delete_front_nodes(l, dist_from_start, mm, n, "next")
            return (n, mm, deleted)
    if half_size != (l.size/2):
        pr = pr.prev
        c1 = pr.value[0]
        r1 = pr.value[1]
        if are_tangent_circles(c1 , r1, c, r):
            deleted = delete_front_nodes(dist_from_start, nn, pr, "pr")
            return (pr, nn, deleted)
    return None

parser = argparse.ArgumentParser()
parser.add_argument("-i", "--items", type=int, help="number of circles to add in graph")
parser.add_argument("-r", "--radious", type=int, help="radius of circles")
parser.add_argument("--min_radious", type=int, help="minimum radius of circles")
parser.add_argument("--max_radious", type=int, help="maximum radius of circles")
parser.add_argument("-b", "--bountary_file", action='store', type=str, help="the file with the walls")
parser.add_argument("-s", "--seed", type=int, default=None, help="seed for random function to create random circles")
parser.add_argument("ouput_file", action='store', type=str, help="the file with the final circles")
args = parser.parse_args()
SEED = args.seed
MIN_RADIOUS = args.min_radious
MAX_RADIOUS = args.max_radious
r = args.radious
ITEMS = args.items
space_limit = None
ouput_file = open(args.ouput_file, "w")
if args.bountary_file != None:
    space_limit = read_file(args.bountary_file)
if SEED != None:
    random.seed(SEED)
    rstart= random.randint(MIN_RADIOUS,MAX_RADIOUS)
else:
    rstart = r
start = (0.00, 0.00)
dist_from_start = {}
c1 = start
ouput_file.write("%.2f %.2f %i\n" % (c1[0], c1[1], rstart))
#print("{:.2f}".format(c1[0]), "{:.2f}".format(c1[1]), rstart, sep=" ")
sdist = round(distance_from_start(c1), 2)
add_in_graph(dist_from_start, sdist, (c1, rstart))
l = linkedlist.Linkedlist((c1, rstart, sdist))
if SEED != None:
    r= random.randint(MIN_RADIOUS,MAX_RADIOUS)
c = (rstart+r, 0.00)
ouput_file.write("%.2f %.2f %i\n" % (c[0], c[1], r))
#print("{:.2f}".format(c[0]), "{:.2f}".format(c[1]), r, sep=" ")
sdist = round(distance_from_start(c), 2)
add_in_graph(dist_from_start, sdist, (c, r))
l.add_last((c, r, sdist))
for i in range(ITEMS - 2):     
    flag = True
    m = find_min_dist(dist_from_start)
    #print(m)
    #print(22222222222222222222222222222222222222222222222)
    #l.printLL()
    prev = l.find_prev(m)
    #print(i)
    #print(prev)
    pr = prev.value
    if space_limit != None:
        deleted = []
        new_list = l.copy()
        cm = prev.next.value
        cm_dead = []
        cm_might_not_dead = []
    if SEED != None:
        r= random.randint(MIN_RADIOUS,MAX_RADIOUS)
    while(flag):
        pr = prev.value
        c = tangent_circle(m[0], m[1], pr[0], pr[1], r)
        ctf = circle_tangert_front(l, dist_from_start, prev, prev.next, c, r)
        #print(22222222222222222222222222222222222222222222222)
        #l.printLL()
        if ctf == None:
            flag = False
        else:
            m = ctf[0].value
            prev = ctf[1]
            if space_limit != None:
                #deleted.append(ctf[2])
                deleted.extend(ctf[2])
            continue
        if space_limit != None:
            limits = check_space_limits(space_limit, c, r)
            flag = limits
            if limits:
                l = new_list.copy()
                for i in range(len(deleted)-1, -1, -1):
                    circle = (deleted[i])[0]
                    index = (deleted[i])[1]
                    dist = circle[2]
                    if dist in dist_from_start:
                        spec_dist = dist_from_start[dist]
                        spec_dist.insert(index, (circle[0], circle[1]))
                    else:
                        dist_from_start[dist] = [(circle[0], circle[1])]
                        #######cm_might_not_dead.append((circle[0], circle[1])
                prev_cm = l.find_prev(cm)
                cm_might_not_dead.clear()
                #l.remove(prev_cm, prev_cm.next.next)
                dist = cm[2]
                listt = dist_from_start[dist]
                listt.remove((cm[0], cm[1]))
                cm_dead.append((cm[0], cm[1], cm[2])) ######
                if not listt:
                    del dist_from_start[dist]
                m = find_min_dist(dist_from_start)
                prev = l.find_prev(m)
                pr = prev.value
                cm = prev.next.value
                deleted = []
                #new_list = l.copy()
            else:
                ###############
                for i in range(len(cm_dead)-1, -1, -1):
                    if cm_dead[i] not in cm_might_not_dead:
                        circle = cm_dead[i]
                        #index = 0
                        dist = circle[2]
                        if dist in dist_from_start:
                            spec_dist = dist_from_start[dist]
                            spec_dist.insert(0, (circle[0], circle[1]))
                        else:
                            dist_from_start[dist] = [(circle[0], circle[1])]



    ouput_file.write("%.2f %.2f %i\n" % (c[0], c[1], r))
    #print("{:.2f}".format(c[0]), "{:.2f}".format(c[1]), r, sep=" ")
    sdist = round(distance_from_start(c), 2)
    add_in_graph(dist_from_start, sdist, (c, r))
    l.add(prev, (c ,r , sdist))
if space_limit:
    for l in space_limit:
        ouput_file.write("%.1f %.1f %.1f %.1f\n" % ((l[0])[0], (l[0])[1], (l[1])[0], (l[1])[1]))
        #print("{:.2f}".format((l[0])[0]), "{:.2f}".format((l[0])[1]), "{:.2f}".format((l[1])[0]), "{:.2f}".format((l[1])[1]), sep=" ")
ouput_file.close()
'''
space_limit = None
space_limit = []
space_limit.append(((150, 96.60), (-150, 96.60)))
space_limit.append(((-150, 96.60), (-150, -96.60)))
space_limit.append(((-150, -96.60), (150, -96.60)))
space_limit.append(((150, -96.60), (150, 96.60)))
SEED = None #13
MIN_RADIOUS = 5
MAX_RADIOUS = 10
r = 10
ITEMS = 119
if SEED != None:
    random.seed(SEED)
    rstart= random.randint(MIN_RADIOUS,MAX_RADIOUS)
else:
    rstart = r
start = (0.00, 0.00)
dist_from_start = {}
l = linkedlist.Linkedlist()
c1 = start
print("{:.2f}".format(c1[0]), "{:.2f}".format(c1[1]), rstart, sep=" ")
sdist = round(distance_from_start(c1), 2)
add_in_graph(dist_from_start, sdist, (c1, rstart))
l = linkedlist.Linkedlist((c1, rstart, sdist))
#l.add_last((c1, rstart, sdist))
if SEED != None:
    r= random.randint(MIN_RADIOUS,MAX_RADIOUS)
c = (rstart+r, 0.00)
print("{:.2f}".format(c[0]), "{:.2f}".format(c[1]), r, sep=" ")
sdist = round(distance_from_start(c), 2)
add_in_graph(dist_from_start, sdist, (c, r))
l.add_last((c, r, sdist))
for i in range(ITEMS - 2):
    flag = True
    m = find_min_dist(dist_from_start)
    prev = l.find_prev(m)
    pr = prev.value
    if space_limit != None:
             limits = check_space_limits(space_limit, c, r)
             flag = limits
             if limits:
                 for i in range(len(deleted)-1, -1,-1):
                     add_again(dist_from_start, l, deleted[i])
                 prev_cm = l.find_prev(cm)
                 l.remove(prev_cm, prev_cm.next.next)

                 dist = cm[2]
                 listt = dist_from_start[dist]
                 listt.remove((cm[0], cm[1]))
                 if not listt:
                     del dist_from_start[dist]

                 #cm = None
                 m = find_min_dist(dist_from_start)
                 prev = l.find_prev(m)
                 pr = prev.value
                 cm = prev.next.value
                 deleted = []

    print("{:.2f}".format(c[0]), "{:.2f}".format(c[1]), r, sep=" ")
    sdist = round(distance_from_start(c), 2)
    add_in_graph(dist_from_start, sdist, (c, r))
'''


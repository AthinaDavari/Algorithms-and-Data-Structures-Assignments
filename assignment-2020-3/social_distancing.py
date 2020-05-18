import math
import linkedlist

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
    return d

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

def delete_front_nodes(listt, dist_from_start, node1, node2, type):
    if type == "pr":
        flag = True
        middle = node1.prev
        while(flag):
            dist = middle.value[2]
            l = dist_from_start[dist]
            l.remove((middle.value[0], middle.value[1]))
            if not l:
                del dist_from_start[dist]
            listt.remove(middle.prev, middle.next)
            middle = middle.prev
            if middle == node2:
                flag = False
        return
    #listt.printLL()
    flag = True
    middle = node1.next
    while(flag):
        dist = middle.value[2]        
        l = dist_from_start[dist]
        #print(middle.value)
        #print("#######")
        #listt.printLL()
        l.remove((middle.value[0], middle.value[1]))
        if not l:
            #dist_from_start.pop(dist, None)
            del dist_from_start[dist]
        #print("#######")
        #listt.printLL()
        #print(middle.prev.value, middle.value,middle.next.value)
        listt.remove(middle.prev, middle.next)
        #listt.printLL()
        middle = middle.next 
        #print(middle.value, node2.value)
        #print(middle == node2)
        if middle == node2:
            flag = False

def circle_tangert_front(l, dist_from_start, pr, n, c, r):
    half_size = math.floor(l.size/2)
    nn = n
    mm = pr
    cn = n.value[0]
    rn = n.value[1]
    cm = pr.value[0]
    rm = pr.value[1]
    for i in range(half_size):
        ''' 
        n = n.next
        c1 = n.value[0]
        r1 = n.value[1]
        if are_tangent_circles(c1 , r1, c, r):
            #l.printLL()
            delete_front_nodes(l, dist_from_start, mm, n, "next")
            #print(n.value, mm.value)
            return (mm, n)
        '''
        pr = pr.prev
        c1 = pr.value[0]
        r1 = pr.value[1]
        if are_tangent_circles(c1 , r1, c, r):
            #l.printLL()
            delete_front_nodes(l, dist_from_start, nn,  pr, "pr")
            return (pr, nn)
        
        n = n.next
        c1 = n.value[0]
        r1 = n.value[1]
        if are_tangent_circles(c1 , r1, c, r):
            #l.printLL()
            delete_front_nodes(l, dist_from_start, mm, n, "next")
            return (mm, n)
        
    if half_size != (l.size/2):
        '''
        n = n.next
        c1 = n.value[0]
        r1 = n.value[1]
        if are_tangent_circles(c1 , r1, c, r):
            #l.printLL()
            delete_front_nodes(l, dist_from_start, mm, n, "next")
            return (mm, n)
        '''
        pr = pr.prev
        c1 = pr.value[0]
        r1 = pr.value[1]
        if are_tangent_circles(c1 , r1, c, r):
            delete_front_nodes(dist_from_start, nn, pr, "pr")
            return (nn, pr)
        
        #print(mm.value, nn.value)
    return None

r = 10
start = (0.00, 0.00)
dist_from_start = {}
l = linkedlist.Linkedlist()
c1 = start
print("{:.2f}".format(c1[0]), "{:.2f}".format(c1[1]), r, sep=" ")
sdist = round(distance_from_start(c1), 2)
add_in_graph(dist_from_start, sdist, (c1, r))
l.add_last((c1, r, sdist))
c = (2*r, 0.00)
print("{:.2f}".format(c[0]), "{:.2f}".format(c[1]), r, sep=" ")
sdist = round(distance_from_start(c), 2)
add_in_graph(dist_from_start, sdist, (c, r))
l.add_last((c, r, sdist)) 
for i in range(998):
    flag = True
    m = find_min_dist(dist_from_start)
    prev = l.find_prev(m)
    pr = prev.value
    while(flag):
        '''
        m = find_min_dist(dist_from_start)
        prev = l.find_prev(m)
        '''
        pr = prev.value
        #print(m[0], pr[0])
        c = tangent_circle(m[0], r, pr[0], r, r)
        #print("miaw")
        #print(c)
        #print("******************")
        #l.printLL()
        #print("******************")
        ctf = circle_tangert_front(l, dist_from_start, prev, prev.next, c, r)
        if ctf == None:
            flag = False
        else:
            m = ctf[1].value
            prev = ctf[0]
            #print("bourrrrrrrrrr")
            #print(m, prev.value)
        #print(flag, " flag")
    print("{:.2f}".format(c[0]), "{:.2f}".format(c[1]), r, sep=" ")
    sdist = round(distance_from_start(c), 2)
    add_in_graph(dist_from_start, sdist, (c, r))
    l.add(prev, (c ,r , sdist))

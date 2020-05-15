class Linkedlist:

    def __init__(self, value=None):
        if value == None:
            self.first = None
            self.size = 0
        else:
            self.first = Node(value)
            self.size = 1
        self.last = None

    def add_last(self, value):
        if self.size == 0:
            self.first = Node(value)
            self.size += 1
        elif self.size == 1:
            node = Node(value, self.first, self.first)
            self.first.next = node
            self.last = node
            self.first.prev = self.last
            self.size += 1
        else:
            node = Node(value, self.last, self.first)
            self.last.next = node
            self.last = node
            self.first.prev = self.last
            self.size += 1
    
    def find_prev(self, value):
        for x in range(self.size):
            if x == 0:
                node = self.last
            else:
                node = node.prev
            if node.value == value:
                return node.prev
        return None

    def add(self, prev, value):
        next = prev.next
        node = Node(value, prev, next)
        prev.next = node
        next.prev = node
        self.size += 1


    def remove_node(self, value):
        for x in range(self.size):
            if x == 0:
                node = self.first
            else:
                node = node.next
            if node.value == value:
                pr = node.prev
                n = node.next
                pr.next = n
                n.prev = pr
                if x == 0:
                    self.first = n
                elif x == self.size - 1:
                    self.last = pr
                self.size -= 1
                return
    
    def remove(self, pr, n):
        if pr.next.value == self.first.value:
            self.first = self.first.next
        if pr.next.value == self.last.value:
            self.last = self.last.prev
        pr.next, n.prev = n, pr
        self.size -= 1

    def printLL(self):
        for x in range(self.size):
            if x == 0:
                node = self.first
                print(node.value)
            else:
                node = node.next
                print(node.value)

class Node:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

if __name__ == "__main__":
    l = Linkedlist(3)
    l.add_last(5)
    l.add_last(8)
    l.add_last(10)
    v = l.find_prev(10)
    l.remove(v, v.next.next)
    l.printLL()
    l.add(v, 6)
    #l.remove_node(10)
    print(l.last.value)
    k =l.find_prev(5)
    print(k.value)
    l.printLL()

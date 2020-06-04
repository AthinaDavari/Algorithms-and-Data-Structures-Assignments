class Linkedlist:
    def __init__(self, value):
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
                node = self.first
            else:
                node = node.next
            if node.value == value:
                return node.prev
        return None

    def add(self, prev, value):
        next = prev.next
        node = Node(value, prev, next)
        prev.next = node
        next.prev = node
        if prev == self.last:
            self.last = node
        self.size += 1
    
    def remove(self, pr, n):
        if pr.next.value == self.first.value:
            self.first = self.first.next
        if pr.next.value == self.last.value:
            self.last = self.last.prev
        pr.next, n.prev = n, pr
        self.size -= 1

    def copy(self):
        if self.size == 0:
            return Linkedlist()
        node = self.first
        new_list = Linkedlist(self.first.value)
        if self.size == 1:
            return new_list
        while(True):
            node = node.next
            new_list.add_last(node.value)
            if node == self.last:
                break
        return new_list

class Node:
    def __init__(self, value, prev=None, next=None):
        self.prev = prev
        self.value = value
        self.next = next

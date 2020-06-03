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

if __name__ == "__main__":
    l = Linkedlist()
    l.add_last(3)
    l.add_last(5)
    l.add_last(8)
    l.add_last(10)
    new_list = l.copy()
    v = l.find_prev(3)
    l.remove(v, v.next.next)
    print("########")
    l.printLL()
    print("########")
    new_list.printLL()
    print("########")
    l.add(v, 6)
    #l.remove_node(10)
    print(l.last.value)
    k =l.find_prev(5)
    print(k.value)
    print("########")
    l.printLL()
    print("########")
    new_list.printLL()

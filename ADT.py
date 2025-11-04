class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link


class Taillinkedlist:
    def __init__(self):
        self._head = None
        self._tail = None

    def add_first(self, item):
        self._head = Node(item, self._head)
        if self._tail is None:
            self._tail = self._head

    def add_last(self, item):
        new_node = Node(item)
        if self._head is None:
            self._head = self._tail = Node(item)
            return self._head

        self._tail.link = new_node
        self._tail = new_node
        return self._head


    def remove_last(self):
        if self._tail is None:
            return None

        if self._head == self._tail:
            data = self._head.data
            self._head = self._tail = None
            return data

        current = self._head
        while current.link is not None:
            current = current.link
        data = self._tail.data
        self._tail = current
        return data

    def remove_first(self):
        if self._head is None:
            return None

        data = self._head.data
        self._head = self._head.link
        if self._head is None:
            self._tail = None
        return data





    def print_list(self):
        if self._head is None:
            return None
        current = self._head
        while current:
            print(current.data, end='->')
            current = current.link
        print("None")

#--------------------------------------------

class Queue:
    def __init__(self):
        self._L = []

    def enqueue(self, item):
        self._L.append(item)

    def dequeue(self):
        return self._L.pop(0)

    def insert_enqueue(self, item):
        self._L.insert(0, item)

    def desert_dequeue(self):
        return self._L.pop()

    #for print only!!!
    def return_lst(self):
        return self._L


class TailQueue:
    def __init__(self):
        self.ll = Taillinkedlist()

    def enqueue(self, item):
        self.ll.add_last(item)

    def dequeue(self):
        return self.ll.remove_first()

    def print_queue(self):
        return self.ll.print_list()


class Stack:
    def __init__(self):
        self._L = []
    def push(self, item):
        self._L.append(item)
    def pop(self):
        return self._L.pop()


class TailStack:
    def __init__(self):
        self._ll = Taillinkedlist()

    def push(self, item):
        self._ll.add_last(item)

    def pop(self):
        return self._ll.remove_last()


class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

class Mapping:
    def __init__(self):
        self._L = []

    def put(self, key, value):
        for e in self._L:
            if e.key == key:
                e.value = value
                return
        self._L.append(Entry(key, value))

    def get(self, key):
        for e in self._L:
            if e.key == key:
                return e.value
        raise KeyError


if __name__ == "__main__":
    print("=== Testing Taillinkedlist ===")

    ll = Taillinkedlist()
    print("Add first (10):")
    ll.add_first(10)
    ll.print_list()

    print("Add first (5):")
    ll.add_first(5)
    ll.print_list()

    print("Add last (20, 30):")
    ll.add_last(20)
    ll.add_last(30)
    ll.print_list()

    print("Remove first:", ll.remove_first())
    ll.print_list()

    print("Remove last:", ll.remove_last())
    ll.print_list()

    print("Remove remaining items:")
    print("Removed:", ll.remove_first())
    print("Removed:", ll.remove_first())
    ll.print_list()

    print("Remove from empty list (should be None):", ll.remove_first())
    print("Remove last from empty (should be None):", ll.remove_last())
    print()

    print("=== Testing Queue (list-based) ===")
    q = Queue()
    for i in range(1, 6):
        q.enqueue(i)
    print("After enqueue 1–5:", q.return_lst())
    print("Dequeue:", q.dequeue())
    print("Dequeue:", q.dequeue())
    print("After two dequeues:", q.return_lst())
    q.insert_enqueue(0)
    print("After insert_enqueue(0):", q.return_lst())
    print("Desert dequeue (from back):", q.desert_dequeue())
    print("After desert_dequeue:", q.return_lst())
    print()

    print("=== Testing TailQueue (linked-list-based queue) ===")
    q_ll = TailQueue()
    for j in range(1, 6):
        q_ll.enqueue(j)
    print("Queue after enqueue 1–5:")
    q_ll.print_queue()
    print("Dequeue:", q_ll.dequeue())
    print("Dequeue:", q_ll.dequeue())
    print("After dequeues:")
    q_ll.print_queue()
    print("Dequeue remaining:")
    print(q_ll.dequeue())
    print(q_ll.dequeue())
    print(q_ll.dequeue())  # should be None now
    print()

    print("=== Testing Stack (list-based) ===")
    s = Stack()
    for x in [10, 20, 30]:
        s.push(x)
    print("Stack after pushes:", s._L)
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    print("Pop:", s.pop())
    try:
        print("Pop empty stack (should raise):")
        print(s.pop())
    except IndexError:
        print("Caught IndexError as expected")
    print()

    print("=== Testing TailStack (linked-list-based stack) ===")
    ts = TailStack()
    print("Pop empty (should be None):", ts.pop())
    ts.push('A')
    ts.push('B')
    ts.push('C')
    print("After pushes A,B,C:")
    ts._ll.print_list()
    print("Pop:", ts.pop())
    print("Pop:", ts.pop())
    print("Pop:", ts.pop())
    print("Pop empty again (should be None):", ts.pop())
    print()

    print("=== Testing Mapping (key-value store) ===")
    m = Mapping()
    m.put("k1", 100)
    print("Get k1:", m.get("k1"))
    m.put("k1", 200)
    print("After overwriting k1:", m.get("k1"))
    m.put("k2", "v2")
    m.put("k3", [1, 2, 3])
    print("Get k2:", m.get("k2"))
    print("Get k3:", m.get("k3"))
    try:
        print("Get missing key:")
        print(m.get("missing"))
    except KeyError:
        print("Caught KeyError as expected")

    print("\n=== All manual tests finished ===")


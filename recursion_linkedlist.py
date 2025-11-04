class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

def print_nodes(node=None):
    if node is not None:
        return
    print(node.data, end=" -> ")
    print_nodes(node.link)

class LinkedList:
    def __init__(self):
        self._head = None

    def add_first(self, item):
        if self._head is None:
            self._head = Node(item)
        else:
            new_node = Node(item)
            new_node.link = self._head
            self._head = new_node
        return self._head
    
    def add_last(self, item):
        if self._head is None:
            self._head = Node(item)
        else:
            current = self._head
            while current.link is not None:
                current = current.link
            new_node = Node(item)
            current.link = new_node
            new_node.link = None
        return self._head
        
    def remove_first(self):
        if self._head is None:
            return
        else:
            current = self._head
            self._head = current.link
            return self._head

    def remove_last(self):
        if self._head is None:
            return
        else:
            current = self._head
            while current.link.link is not None:
                current = current.link
            current.link = None
            return self._head
        
    def __contains__(self, item):
        if self._head is None:
            return False
        else:
            current = self._head
            while current is not None:
                if current.data == item:
                    return True
                current = current.link
            return False
        
    def __len__(self):
        current = self._head
        counter = 0
        while current is not None:
            counter += 1
            current = current.link
        return counter
    
    def __iter__(self):
        current = self._head
        while current is not None:
            yield current.data
            current = current.link
    
    def recursion_print(self, current=None):

        if current is None:
            current = self._head

        if current is None:
            print("None")
            return

        print(current.data, end=" -> ")

        if current.link is not None:
            self.recursion_print(current.link)
        else:
            print("None")

    def __getitem__(self, index): 
        current = self._head 
        first_index = 0 
        while first_index < index and current is not None: 
            current = current.link 
            first_index += 1 
        if index == first_index: 
            return current.data 
        else: 
            raise IndexError

    def __setitem__(self, index, item):
        current = self._head
        first_index = 0 
        while first_index < index and current is not None: 
            current = current.link 
            first_index += 1
        if first_index == index:
            current.data = item


    def reverse_recursive(self, current):
        if current is None or current.link is None:
            return current
        
        next_node = current.link
        current.link = None
        new_head = self.reverse_recursive(next_node)
        next_node.link = current
        return new_head
    

    def call_printer(self):
        print_nodes(self._head)
    



if __name__ == '__main__':
    lst = LinkedList()
    lst.add_last(1)
    lst.add_last(2)
    lst.add_last(3)
    for i in lst:
        print(i, end=' -> ')
    print()

    lst.remove_last()
    for i in lst:
        print(i, end=' -> ')
    print()

    lst.add_first(4)
    lst.add_first(5)
    for i in lst:
        print(i, end=' -> ')
    print()

    lst.remove_first()
    for i in lst:
        print(i, end=' -> ')
    print()

    print(lst.__contains__(1))
    print(lst.__contains__(17))

    for i in lst:
        print(i, end=' -> ')
    print()
    
    print(f'Number of Nodes: {len(lst)}')
    
    lst.recursion_print()

    print(lst.__getitem__(0))

    lst.__setitem__(1, 5)
    for i in lst:
        print(i, end=' -> ')

    '''
    lst.reverse_recursive()
    for i in lst:
        print(i, end=' -> ')'''

    print("\n\n\n")
    print_nodes()

    
   
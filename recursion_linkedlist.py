class Node:
    def __init__(self, item, next_node=None):
        self.data = item
        self.link = next_node


def add_last(node, item):
    if node.link is None:
        node.link = Node(item)
    else:
        add_last(node.link, item)


def print_ll(node):
    if node is None:
        return
    print(node.data, end=' -> ')
    print_ll(node.link)


def print_ll_reversed(node):
    if node is None:
        return
    print_ll_reversed(node.link)
    print(node.data, end=' -> ')


def contain(node, item):
    if node is None:
        return False
    if node.data == item:
        return True
    return contain(node.link, item)


def count_node(node):
    if node is None:
        return 0
    return 1 + count_node(node.link)


def reversed(node):
    if node.link is not None:
        yield from reversed(node.link)
    yield node.data


def iter(node):
    yield node.data
    if node.link is not None:
        yield from iter(node.link)


def sum_nodes(node):
    if node is None:
        return 0
    return node.data + sum_nodes(node.link)


def remove_last(node):
    if node is None or node.link is None:
        return None
    if node.link.link is None:
        item = node.link.data
        node.link = None
        return item
    return remove_last(node.link)


def get_last(node):
    if node.link is None:
        return node.data
    return get_last(node.link)


def get_index(node, element):
    if node is None or element < 0:
        raise IndexError("Index out of range")
    if element == 0:
        return node.data
    if node and node.link:
        return get_index(node.link, element - 1)
    raise IndexError


def min_value(node):
    if node.link is None:
        return node.data
    return min(node.data, min_value(node.link))


def max_value(node):
    if node.link is None:
        return node.data
    return max(node.data, max_value(node.link))


class LinkedList:
    def __init__(self):
        self._head = None

    def add_first(self, item):
        new_node = Node(item)
        new_node.link = self._head
        self._head = new_node

    def add_last(self, item):
        if self._head is None:
            self.add_first(item)
        else:
            add_last(self._head, item)

    def print_ll(self):
        if self._head is None:
            print("Empty list")
        else:
            print_ll(self._head)
            print()

    def print_ll_reversed(self):
        if self._head is None:
            print("Empty list")
        else:
            print_ll_reversed(self._head)
            print("None")

    def __contains__(self, item):
        return contain(self._head, item)

    def __len__(self):
        return count_node(self._head)

    def sum_nodes(self):
        return sum_nodes(self._head)

    def remove_first(self):
        if self._head is None:
            return
        self._head = self._head.link

    def remove_last(self):
        if self._head is None:
            return
        elif self._head.link is None:
            self._head = None
        else:
            remove_last(self._head)

    def get_last(self):
        if self._head is None:
            return None
        return get_last(self._head)

    def get_index(self, element):
        return get_index(self._head, element)

    def min_value(self):
        if not self._head:
            return
        return min_value(self._head)

    def max_value(self):
        if self._head is None:
            return None
        return max_value(self._head)


if __name__ == '__main__':
    ll = LinkedList()
    ll.add_first(3)
    ll.add_first(2)
    ll.add_first(1)
    ll.add_last(4)
    ll.add_last(5)
    ll.add_last(6)

    print("Linked list:")
    ll.print_ll()
    print("\nReversed linked list:")
    ll.print_ll_reversed()
    print("\n")

    print("Contains 2:", 2 in ll)
    print("Contains 5:", 5 in ll)

    print("Length of linked list:", len(ll))

    print("Sum of all nodes:", ll.sum_nodes())

    print("Last element:", ll.get_last())

    ll.remove_first()
    print("After removing first element:")
    ll.print_ll()
    print()

    ll.remove_last()
    print("After removing last element:")
    ll.print_ll()
    print()

    try:
        print("Element at index 2:", ll.get_index(2))
    except IndexError as e:
        print("Index error:", e)

    print("Minimum value in list:", ll.min_value())
    print("Maximum value in list:", ll.max_value())
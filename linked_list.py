class Node:
    def __init__(self, data, link=None):
        self.data = data
        self.link = link

class Linkedlist:
    #__init__
    def __init__(self):
        self._head = None

    # add_first
    def add_first(self, item):
        self._head = Node(item, self._head)

    # add_last
    def add_last(self, item):
        if self._head is None:
            self.add_first(item)
        node = self._head
        while node.link is not None:
            node = node.link
        node.link = Node(item)

    #remove_first
    def remove_first(self):
        if self._head is None:
            raise IndexError
        if self._head is not None:
            data = self._head.data
            self._head = self._head.link
            return data

    #remove_last
    def remove_last(self):
        if self._head is None:
            raise IndexError
        if self._head.link is None:
            data = self._head.data
            self._head = None
            return data
        current = self._head
        while self._head.link.link is not None:
            current = current.link
        data_l = self._head.link.data
        self._head.link = None
        return data_l

    #sum_data
    def sum_data(self):
        total=0
        if self._head is None:
            return total
        current=self._head
        while current is not None:
            total +=current.data
            current=current.link
        return total

    #node_counters
    def node_counters(self):
        counter = 0
        if self._head is None:
            return counter
        current=self._head
        while current is not None:
            counter +=1
            current = current.link
        return counter

    #count_negative
    def count_negative(self):
        count=0
        if self._head is None:
            return count
        cur= self._head
        while cur is not None:
            if cur.data < 0:
                count +=1
            cur=cur.link
        return count

    #count_positive
    def count_positive(self):
        count = 0
        if self._head is None:
            return count
        current = self._head
        while current is not None:
            if current.data > 0:
                count += 1
            current = current.link
        return count

    #reverse
    def reverse_ll(self):
        if self._head is None:
            return None
        previous = None
        current = self._head
        #after = current.link

        while current is not None:
            after = current.link
            current.link, previous, current = previous, current, after

        self._head = previous
        return self._head

    def change_element(self, element, new_element):
        change = False
        if self._head is None:
            raise IndexError
        cur = self._head
        while cur is not None:
            if cur.data == element:
                cur.data = new_element
                change = True
            cur = cur.link
        return change

    #__contains__
    def __contains__(self, item):
        if self._head is None:
            return False

        current = self._head
        while current is not None:
            if current.data == item:
                return True
            current = current.link
        return False

    #__len__
    def __len__(self):
        counter = 0
        if self._head is None:
            return counter
        current = self._head
        while current is not None:
            counter += 1
            current = current.link
        return counter

    #__getitem__
    def __getitem__(self, index):
        if self._head is None:
            raise IndexError
        if index < 0 :
            raise IndexError

        count = 0
        current = self._head
        while current is not None:
            if count == index:
                return current.data
            count += 1
            current = current.link

    #__setitem__
    def __setitem__(self, index, new_element):
        if self._head is None:
            raise IndexError
        ind = 0
        node = self._head
        while node is not None:
            if ind == index:
                node.data = new_element
                return True
            ind += 1
            node = node.link
        raise IndexError

    #iter
    def __iter__(self):
        if self._head is None:
            return None
        current = self._head
        while current is not None:
            yield current.data
            current = current.link

    #iter with next
    def __iter__(self):
        #def __iter__(self):
        #return LinkedListIterator(self._head)
        '''class LinkedListIterator:
                def __init__(self, head):
                       self._current = head
                def __iter__(self, item):
                      return self
                def __next__(self):
                    if self._current is None:
                         raise StopIteration
                    else:
                        data = self._current.data
                        self._current = self._current.link
                    return data'''
        self._current = self._head
        return self

    #__next__
    def __next__(self):
        if self._current is None:
            raise StopIteration
        data = self._current.data
        self._current = self._current.link
        return data

    #__str__
    def __str__(self):
        if self._head is None:
            return "None"
        texet=""
        current=self._head
        while current is not None:
            texet += f"{current.data} -> "
            current=current.link
        texet += "None"
        return texet

    def print_ll(self):
        if self._head is None:
            print("None")
            return
        current = self._head
        while current is not None:
            print(current.data, end="->")
            current = current.link
        print("None")
        return

    def sum_even_nodes(self):
        total = 0
        if self._head is None:
            return total

        current = self._head
        index_of_nodes = 0
        while current is not None:
            if index_of_nodes % 2 == 0:
                total += current.data
            current = current.link
            index_of_nodes += 1
        return total

    #20 -> 30 -> 40 -> 1000 -> 60 -> -100 -> -50 -> 99999 -> None
    def sum_odd_nodes(self):
        total = 0
        if self._head is None:
            return total

        current = self._head
        index_of_nodes = 0
        while current is not None:
            if index_of_nodes % 2 == 1:
                total += current.data
            current = current.link
            index_of_nodes += 1
        return total

    '''
    summan = 0
    index = 0
    #20 -> 30 -> 40 -> 1000 -> 60 -> -100 -> -50 -> 99999 -> None
    #0           2             4              6
    current = self._head
    while current is not None:
        if index % 2 == 0:
            summan += current.data
        current = current.link
        index += 1
    return summan
    '''

    def change_first_and_last(self, first, last):
        pass

    def change_mid_to_negative(self, element):
        pass


if __name__ == "__main__":
    ll = Linkedlist()
    try:
        ll.add_first(30)
        ll.add_first(20)
        ll.add_first(10)
    except Exception as e:
        print(e)
    finally:
        ll.print_ll()

    try:
        print("Data deleted: ", ll.remove_first())
    except Exception as e:
        print(e)
    finally:
        ll.print_ll()

    try:
        ll.add_last(40)
        ll.add_last(50)
        ll.add_last(60)
        ll.add_last(-100)
        ll.add_last(-50)
        ll.add_last(50)
    except Exception as e:
        print(e)
    finally:
        ll.print_ll()

    try:
        print("Remove last: ", ll.remove_last())
    except Exception as e:
        print(e)
    finally:
        print("Current Linkedlist: ",end="")
        ll.print_ll()

    try:
        print("Sum Nodes: ", ll.sum_data())
    except Exception as e:
        print(e)

    try:
        print("Positives: ", ll.count_positive())
    except Exception as e:
        print(e)

    try:
        ll.reverse_ll()
    except Exception as e:
        print(e)
    finally:
        print("Reverse", end=" ")
        ll.print_ll()

    try:
        print("Negatives test: ", ll.count_negative())
    except Exception as e:
        print(e)

    try:
        print("reversed: ", end="")
        ll.reverse_ll()
    except Exception as e:
        print(e)
    finally:
        ll.print_ll()

    try:
        value = 50
        new_value = 1000
        check = ll.change_element(value, new_value)
        if check:
            print(f"change_element test, Value changed from {value} to {new_value}, OK!")
        else:
            print(f"change_element test, Value not changed from {value} to {new_value}, Not OK!")

        value = 999
        new_value = 100
        check = ll.change_element(value, new_value)
        if not check:
            print(f"change_element test, value not exist!, OK!")
        else:
            print(f"change_element test, Error!, Not OK!")
    except Exception as e:
        print(e)
    finally:
        ll.print_ll()

    try:
        check = ll.__contains__(-50)
        if check:
            print("Contain test, is OK!")
        else:
            raise ValueError("Contain test, Value Error")
        check = ll.__contains__(200)
        if not check:
            print("Contain test, Not Contain OK!")
        else:
            raise ValueError("Contain test, Value Error")
    except Exception as e:
        print(e)


    try:
        lens = ll.__len__()
        if lens == 8:
            print("len Test OK!", True)
        else:
            print("len test Not OK!", False)
    except Exception as e:
        print(e)

    try:
        currently = ll.__iter__()
        print("iterator test: ", end="")
        for number in currently:
            print(number, end="->")
        print("None")
    except Exception as e:
        print(e)

    try:
        elem=7
        new_val=99999
        currently = ll.__setitem__(elem, new_val)
        if currently:
            print("setitem test, item has been updated, ok!")
        else:
            print("setitem test, item has not updated, not ok!")
    except Exception as e:
        print(e)

    try:
        pos = 3
        currently = ll.__getitem__(pos)
        if currently == 1000:
            print(f"getitem test, item is exists {currently}, test OK!")
        else:
            print("getitem test, Error!, Not OK!")
    except Exception as e:
        print(e)

    try:
        iterator = iter(ll)
        print("Next test: ",end="")
        for i in range(ll.__len__()):
            print(f"{next(iterator)} -> ", end="")
        print("None")
    except Exception as e:
        print(e)

    try:
        correct_str = "20 -> 30 -> 40 -> 1000 -> 60 -> -100 -> -50 -> 99999 -> None"
        result = ll.__str__()
        if result == correct_str:
            print("String test, OK!")
        else:
            print("String test, Not OK!")
    except Exception as e:
        print(e)

    try:
        check = ll.sum_even_nodes()
        if check == 70:
            print(f"sum even nodes test, {check} OK!")
        else:
            print("sum even nodes test not OK!")
    except Exception as e:
        print(e)

    try:
        test = ll.sum_odd_nodes()
        if test == 100929:
            print(f"sum odd nodes test, {test} OK!")
        else:
            print("sum odd nodes test not OK!")
    except Exception as e:
        print(e)
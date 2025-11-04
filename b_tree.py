class BinaryTree:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def preorder(self):
        print(self.data, end=" ")
        if self.left:
            self.left.preorder()

        if self.right:
            self.right.preorder()

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.data, end=" ")

        if self.right:
            self.right.inorder()

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.data, end=" ")

    def sum_of_nodes(self):
        total = 0
        if self.data is None:
            return total
        total += self.data

        if self.left:
            total += self.left.sum_of_nodes()

        if self.right:
            total += self.right.sum_of_nodes()
        return total

    def count_negatives(self):
        counter = 0
        if self is None:
            return counter
        if self.data < 0:
            counter += 1
        if self.left:
            counter += self.left.count_negatives()

        if self.right:
            counter += self.right.count_negatives()
        return counter

    def count_positives(self):
        counter = 0
        if self is None:
            return counter
        if self.data > 0:
            counter += 1
        if self.left:
            counter += self.left.count_positives()

        if self.right:
            counter += self.right.count_positives()
        return counter

    def count_leaves(self):
        counter = 0
        if self is None:
            return counter
        if not self.left and not self.right:
            counter += 1
        if self.left:
            counter += self.left.count_leaves()
        if self.right:
            counter +=  self.right.count_leaves()

        return counter

    def count_parents(self):
        counter = 0
        if self is None:
            return counter
        if self.left or self.right:
            counter += 1
        if self.left:
            counter += self.left.count_parents()
        if self.right:
            counter += self.right.count_parents()
        return counter

    def height(self):
        counter=0
        if self is None:
            return counter

        left=0
        right=0
        if self.left:
             left = self.left.height()

        if self.right:
            right = self.right.height()
        return max(left, right) + 1

    def shortest_path(self):
        counter = 0
        if self is None:
            return counter

        left=0
        right=0
        if self.left:
            left = self.left.shortest_path()

        if self.right:
            right = self.right.shortest_path()
        return min(left, right) + 1

    def change_value(self, item, new_value):
        if self.data is None:
            return False
        if self.data == item:
            self.data = new_value
            return True
        changed = False
        if self.left:
            changed = self.left.change_value(item, new_value)
        if self.right:
            changed = self.right.change_value(item, new_value)
        return changed

    def max_value(self):
        maximum = 0
        if self is None:
            return maximum

        if self.data > maximum:
            maximum = self.data
        if self.left:
            maximum = self.left.max_value()

        if self.right:
            maximum = self.right.max_value()
        return maximum

    def min_value(self):
        minimum = 0
        if self is None:
            return minimum

        if self.data < minimum:
            minimum = self.data

        if self.left:
            minimum = self.left.min_value()
        if self.right:
            minimum = self.right.min_value()
        return minimum
    def has_path_sum(self, total_path):
        if self is None:
            return False

        new_path = total_path - self.data

        if new_path == 0 and not self.left and not self.right:
            return True

        if self.left and self.left.has_path_sum(new_path):
            return True

        if self.right and self.right.has_path_sum(new_path):
            return True

        return False

    def tree_string(self):
        string = """
                           (50)
                         /      \\
                      (20)       (80)
                      /  \\       /  \\
                   (10)  (30) (70)  (90)
                   /                   \\
                (-1)                   (100)
                /
            (-10)
        """
        return string

if __name__ == '__main__':

    tree = BinaryTree()
    print("-------------------------- Tree --------------------------")
    print(tree.tree_string())
    node_a = BinaryTree(50)
    node_b = BinaryTree(20)
    node_c = BinaryTree(80)
    node_d = BinaryTree(10)
    node_e = BinaryTree(30)
    node_f = BinaryTree(70)
    node_g = BinaryTree(90)
    node_h = BinaryTree(-1)
    node_i = BinaryTree(100)
    node_j = BinaryTree(-10)

    node_a.left = node_b
    node_a.right = node_c

    node_b.left = node_d
    node_b.right = node_e

    node_c.left = node_f
    node_c.right = node_g

    node_d.left = node_h

    node_g.right = node_i

    node_h.left = node_j
    print("-----------------------------------------\n----------------- Tests -----------------\n-----------------------------------------\n")
    try:
        print("Preorder")
        node_a.preorder()
    except Exception as e:
        print(e)
    finally:
        print("\n")

    try:
        print("Inorder")
        node_a.inorder()
    except Exception as e:
        print(e)
    finally:
        print("\n")

    try:
        print("Postorder")
        node_a.postorder()
    except Exception as e:
        print(e)
    finally:
        print("\n")

    try:
        print("Total = ", node_a.sum_of_nodes())
        if 439 == node_a.sum_of_nodes():
            print("Total test correct, OK!")
        else:
            print("Total test not correct, Not OK!")
    except Exception as e:
        print(e)
    finally:
        print("\n")

    try:
        print("Negative nodes = ", node_a.count_negatives())
    except Exception as e:
        print(e)

    try:
        print("Positive nodes = ", node_a.count_positives())
    except Exception as e:
        print(e)

    try:
        print("Leaves counter = ", node_a.count_leaves())
    except Exception as e:
        print(e)

    try:
        print("Parents counter = ", node_a.count_parents())
    except Exception as e:
        print(e)

    try:
        print("Height = ", node_a.height())
    except Exception as e:
        print(e)

    try:
            print("shortest path = ", node_a.shortest_path())
    except Exception as e:
        print(e)

    try:
        item = 90
        new_value = 999
        check = node_a.change_value(item, new_value)
        if check:
            print("Value changed, OK!", item)
        else:
            print("Value not changed, Not OK!", item)
    except Exception as e:
        print(e)

    try:
        print("Max value so far: ", node_a.max_value())
    except Exception as e:
        print(e)

    try:
        print("Min value so far: ", node_a.min_value())
    except Exception as e:
        print(e)

    try:
        path = 200
        check = node_a.has_path_sum(path)
        if check:
            print("Path sum changed, OK!")
        else:
            print("Path not changed, Not OK!")
    except Exception as e:
        print(e)
def fibo_iterative(n):
    terms = [0, 1]
    i = 2
    while i<=n:
        terms.append(terms[i-1]+terms[i-2])
        i=i+1
    return terms[n]

print fibo_iterative(10)

def fibo_recursive(n):  
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return (fibo_recursive(n-1) + fibo_recursive(n-2))

print fibo_recursive(10)



class  Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

    def add_left(self, node):
        self.left_child = node

    def add_right(self, node):
        self.right_child = node

    def has_left(self):
        return self.left_child is not None

    def has_right(self):
        return self.right_child is not None

    def get_left(self):
        return self.left_child

    def get_right(self):
        return self.right_child


class BinaryTree:
    def __init__(self, root_letter):
        self.root = Node(root_letter)
    
    def add_letter(self, letter):
        self.add_letter_recursive(self.root, Node(letter))

    def print_tree(self):
        self.print_tree_recursive(self.root)

    @staticmethod
    def add_letter_recursive(cur_node, node):
        if node.value < cur_node.value:
            if cur_node.has_left():
                BinaryTree.add_letter_recursive(cur_node.get_left(), node)
            else:
                cur_node.add_left(node)
        elif node.value > cur_node.value:
            if cur_node.has_right():
                BinaryTree.add_letter_recursive(cur_node.get_right(), node)
            else:
                cur_node.add_right(node)

    @staticmethod
    def print_tree_recursive(cur_node):
        if cur_node is None:
            return

        BinaryTree.print_tree_recursive(cur_node.get_left())
        print cur_node.value
        BinaryTree.print_tree_recursive(cur_node.get_right())


tree = BinaryTree("z")
tree.add_letter("q")
tree.add_letter("r")
tree.add_letter("a")
tree.add_letter("f")
tree.print_tree()

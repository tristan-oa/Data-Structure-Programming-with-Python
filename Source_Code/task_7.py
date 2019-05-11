# A class Node for the node objects to be stored in the tree
# This consists of 3 functions: a constructor, an inserting()
# function and a in_order() function
class Node:

    # A constructor taking 2 parameters which are 'self' and also
    # 'num" which is set to 'None' by default
    # All possible nodes in a BST are enlisted
    def __init__(self, num=None):
        self.num = num
        self.left = None
        self.right = None

    # A recursive function which is originally called from the Tree class
    # This simply checks if a value to be entered is less than the root
    # node and if so, calls the function recursively if there already
    # exists a left node, but if not, simply creates one and assigns
    # that value to it. If this value happens to be greater than the root
    # node, a similar procedure is run for the right node instead
    # If the value is neither larger nor smaller than a particular node,
    # then the user is informed that the value already exists in the BST
    def inserting(self, val):
        if self.num > val:
            if self.left:
                self.left.inserting(val)
                print()
            else:
                self.left = Node(val)
                print(val, "is set as a left child")
        elif self.num < val:
            if self.right:
                self.right.inserting(val)
            else:
                self.right = Node(val)
                print(val, "is set as a right child")
        else:
            print("Value already exists in the Binary Search Tree")

    # A recursive function which is originally called from the Tree
    # class. This simply prints out each individual BST number in
    # inorder traversal
    def in_order(self):
        if self:
            if self.left:
                self.left.in_order()
            print(str(self.num))
            if self.right:
                self.right.in_order()


# A class Tree which can be explained as the main interface for
# the user. This class then makes use of the Node class
class Tree:

    # A default constructor which initialises the root node to None
    def __init__(self):
        self.root = None

    # A function which checks if the Root node exists. If so, the
    # inserting() function from the class Node is called and if
    # not, the value entered is initialised as the Root Node
    def insert(self, val):
        print("\nInserting", val, "into the BST")
        if self.root:
            self.root.inserting(val)
        else:
            self.root = Node(val)
            print(val, "is the Root Node")

    # A function which calls the in_order() function from the Node
    # class to be able to print the elements in the BST
    def print_tree(self):
        print("\nPrinting the existing Binary Search Tree using IN ORDER Traversal:")
        self.root.in_order()


print("\t\tWelcome to this program which implements a BINARY SEARCH TREE")
print("------------------------------------------------------------------------------")

# Creating an instance 'values' of the object 'Tree' to be able to make use of
# certain functions
values = Tree()

# Inserting values into the newly created Binary Search Tree
values.insert(5)
values.insert(9)
values.insert(2)
values.insert(15)
values.insert(4)
values.insert(1)
values.insert(6)
values.insert(15)

print("\nAll values were added to the Binary Search Tree (except for repeated ones)")
print("---------------------------------------------------------------------------")

# Printing the values using in order traversal
values.print_tree()

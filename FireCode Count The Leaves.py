class BinaryTree:
    #Write a function to find the total number of leaf nodes in a binary tree.
    #A node is described as a leaf node if it doesn't have any children. If there are no leaf nodes, return 0.

#    Example:
 #      1
  #    / \
   #  2   3     
 #   / \ / \
 #  4  5 6  7
 # / \
# 8   9     
# ==> no. of leaves = 5
    def __init__(self, root_node = None):
            self.root = root_node

    def number_of_leaves(self,root):
        if root is None:
            return 0
        elif root.left_child is None and root.right_child is None:
            return 1
        else:
            return self.number_of_leaves(root.left_child) + self.number_of_leaves(root.right_child)

from binary_tree import Binarytree
from node import Node

tree = Binarytree(Node(6))

nodes = [5, 3, 9, 7, 8, 7.5, 12, 11]

for n in nodes:
    tree.add(Node(n))

tree.delete(9)
tree.inorder()

#tree = Binarytree(Node(9))
#tree.add(Node(5))
#tree.add(Node(11))
#
#tree.inorder()
#print(tree.find(11))
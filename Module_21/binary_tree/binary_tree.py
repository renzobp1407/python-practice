from node import Node

class Binarytree:
    def __init__(self, head: Node):
        self.head = head
        
    def add(self, new_node: Node):
        current_node = self.head
        while current_node:
            if new_node.value == current_node.value:
                raise ValueError('A node with that value already exists.')
            elif new_node.value < current_node.value:
                if current_node.left:
                    current_node = current_node.left
                    break
            else:
                if current_node.right:
                    current_node = current_node.right
                else:
                    current_node.right = new_node
                    break
                
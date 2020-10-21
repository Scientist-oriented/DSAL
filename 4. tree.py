# Binary Search Tree 만들기

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class NodeCon:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        node = self.head
        while True:
            if node.value > value:
                if node.left == None:
                    node.left = Node(value)
                    break
                else:
                    node = node.left
            else:
                if node.right == None:
                    node.right = Node(value)
                    break
                else:
                    node = node.right

    def search(self, value):
        node = self.head
        while node:
            if node.value == value:
                print(value, " Found in the Tree")
                return
            elif node.value > value:
                node = node.left
            else:
                node = node.right
        print("Not Found in the Tree")

tree_head = Node(1)
tree = NodeCon(tree_head)

tree.insert(2)
tree.insert(3)
tree.insert(0)
tree.insert(4)
tree.insert(8)

tree.search(1)
tree.search(2)
tree.search(3)
tree.search(10)
tree.search(20)
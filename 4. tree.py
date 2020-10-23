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

    def delete(self, value):
        
        # 삭제하려는 node 찾아가는 과정
        searched = False
        node = self.head
        parent_node = self.head

        while node:
            if node.value == value:
                searched = True
                break
            elif node.value > value:
                parent_node = node
                node = node.left
            else:
                parent_node = node
                node = node.right

        if searched = False:
            print("No data Cannot delete")
            return False

        # 삭제할 node가 leaf node일 경우

        if node.left == None and node.right == None:
            if value < parent_node.value:
                parent_node.left = None
            else:
                parent_node.right = None
            del node

        # 삭제할 node가 child를 하나 가지고 있을 경우

        elif node.left == None or node.right == None:
            if value < parent_node.value:
                parent_node.left = node.right
            else:
                parent_node.right = node.right
            del node

        # 삭제할 node가 child를 두개 가지고 있는 경우

        else:
            if value < parent_node.value:
                sub_node = node.right
                sub_node_parent = node.right
                while sub_node.left:
                    sub_node_parent = sub_node
                    sub_node = sub_node.left
                parent_node.left = 

                


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
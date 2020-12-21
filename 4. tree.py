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
                #print(value, " Found in the Tree")
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

        if searched == False:
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

        elif node.left != None and node.right == None:
            if value < parent_node.value:
                parent_node.left = node.left
            else:
                parent_node.right = node.left
            del node

        elif node.left == None and node.right != None:
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
                sub_node_parent.left = sub_node.right
                parent_node.left = sub_node
                sub_node.left = node.left
                sub_node.right = node.right
                del node
            else:
                sub_node = node.right
                sub_node_parent = node.right
                while sub_node.left:
                    sub_node_parent = sub_node
                    sub_node = sub_node.left
                sub_node_parent.left = sub_node.right
                parent_node.right = sub_node
                sub_node.left = node.left
                sub_node.right = node.right
                del node
                
        print("Data deleted")
        return

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

print("-------------delete test----------------")

import random

test_nums = set()
while len(test_nums) != 100:
    test_nums.add(random.randint(0, 999))

print(test_nums)

test_tree_head = Node(500)
test_tree = NodeCon(test_tree_head)

for nums in test_nums:
    test_tree.insert(nums)

for nums in test_nums:
    test_tree.search(nums)

print("test ready")

test_delete_nums = set()
test_nums_list = list(test_nums)
    # set는 인덱싱이 불가능하다!

while len(test_delete_nums) != 10:
    test_delete_nums.add(test_nums_list[random.randint(0, 99)])

print(test_delete_nums)

for nums in test_delete_nums:
    test_tree.delete(nums)


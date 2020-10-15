class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class nodemngt:
    def __init__(self, head):
        self.head = Node(head)

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def display(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next 


test_list = nodemngt(0)
test_list.display()

for data in range(1, 10):
    test_list.add(data)

test_list.display()


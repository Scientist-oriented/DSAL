class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class nodemngt:
    def __init__(self, head):
        self.head = head

    def add(self, data):
        if self.head == None:
            self.head = node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = node(data)

    def display(self):
        node = self.head
        if node.next == None:
            print(node.data)
        else:
            while node:
                print(node.data)
                node = node.next

test_node = node(1)

test_list = nodemngt(test_node)
test_list.display()


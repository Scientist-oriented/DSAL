class node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class nodemngt:
    def __init__(self, head):
        self.head = head

    def add(self, data):
        if self.head == None:
            self.head = data
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = data

    def display(self):
        node = self.head
        while node:
            print(node)
            node = node.next 


test_list = nodemngt(0)
test_list.display()


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

    def delete(self, data):
        if self.head == None:
            print("Nothing in Linked List")
            return
        elif self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    temp = node.next
                    node.next = node.next.next
                    del temp
                    return
                else:
                    node = node.next
                


# class명을 node라고 했을 때 잘 안되다가 Node 대문자로 바꾸니까 잘 된다.
    # 아마도 변수 값이랑 혼동해서 사용해서 그런 듯?


test_list = nodemngt(0)
test_list.display()

for data in range(1, 10):
    test_list.add(data)

test_list.display()
print("-----------------------")
test_list.delete(9)

test_list.display()


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
            return
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

    def search(self, data):
       node = self.head
       while node:
            if node.data == data:
               print(node.data)
               return
            else:
                node = node.next
       return print("No data")
            


# class명을 node라고 했을 때 잘 안되다가 Node 대문자로 바꾸니까 잘 된다.
    # 아마도 변수 값이랑 혼동해서 사용해서 그런 듯?


test_list = nodemngt(0)

for data in range(1, 10):
    test_list.add(data)

test_list.display()
print("-----------------------")
test_list.delete(0)

test_list.display()

print("......................")
test_list.search(5)
test_list.search(10)

class doubleNode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class dnodemngt:
    def __init__(self, head, tail=None):
        self.head = doubleNode(head)
        self.tail = tail

    def add(self, data):
        if self.head == None:
            self.head = doubleNode(data)
            self.tail = self.head
        
        node = self.head
        while node.next:
            node = node.next
        new = doubleNode(data)
        new.prev = node
        node.next = new
        self.tail = new

    def display(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data): # 특정한 데이터를 가진 노드를 삭제하는 것 (Linked List의 삭제는 연결을 끊는 것)
        if data == self.head.data: # 그 노드가 head일 때
            temp = self.head
            self.head = temp.next # 원래 2번째 node를 head로 만들고
            self.head.prev = None # 그 node의 prev값을 None으로 만들어줌. (연결 끊기)
            temp.next = None # 그리고 삭제할 node의 next값을 None으로 함. (연결 끊기)
            del temp
        elif data == self.tail.data: # 그 노드가 tail일 때
            temp = self.tail 
            self.tail = temp.prev # tail에 삭제되는 node 이전의 node를 할당
            temp.prev = None # 원래 tail에 있던 prev값을 초기화 (연결 끊기)
            self.tail.next = None # 지금 tail이 되는 node에 있는 next값을 삭제 (연결 끊기)
            del temp
        else: # 그 이외 node일 때
            node = self.head
            while node.data != data:
                if node.next == None: # 만약에 없는 node라면
                    print("Data not in the list")
                    return
                node = node.next
            before = node.prev
            after = node.next
            before.next = node.next
            after.prev = node.prev
            del node
            return

    def search_from_top(self, data):
        if self.head == None:
            print("Nothing in the List")
            return

        node = self.head
        while node.data != data:
            if node.next == None:
                print("Data not in the list")
                return
            node = node.next
        print(node.data)

    def search_from_bottom(self, data):
        if self.head == None:
            print("Nothing in the List")
            return

        node = self.tail
        while node.data != data:
            if node.prev == None:
                print("Data not in the list")
                return
            node = node.prev
        print(node.data)


    def insert_before(self, data, before_data):
        if self.head == None:
            print("{} added in the empty list".format(data))
            self.head = doubleNode(data)

        elif before_data == self.head.data:
            temp = self.head
            self.head = doubleNode(data)
            self.head.next = temp
            temp.prev = self.head

        else:
            node = self.tail
            while node.data != before_data:
                if node == None:
                    print("No before data found!")
                    return
                else:
                    node = node.prev

            # 이 코드를 while문 안에 넣어놔서 마지막 줄에 있는 return 때문에 while문이 한바퀴만 돌아서 개고생함.
            # 무슨 짓을 해도 무조건 node값이 9로 고정이 되길래 위에 while문이 잘 못된 것만 찾았는데 아니었음.
            # 역시 코드는 거짓말을 하지 않는다.
            new = doubleNode(data)
            before_new = node.prev
            node.prev = new
            before_new.next = new
            new.prev = before_new
            new.next = node
            return


            


print("-----------------DLL Display----------------------")

DLL1 = dnodemngt(0)
DLL1.display()

print("-----------------DLL ADD Test----------------------")

for i in range(1, 11):
    DLL1.add(i)

DLL1.display()

print("-----------------DLL Delete Test----------------------")

DLL1.delete(4)
DLL1.delete(0)
DLL1.delete(10)
DLL1.display()
DLL1.delete(11)

print("-----------------DLL search_from Test------------------")

DLL1.search_from_top(3)
DLL1.search_from_bottom(2)

print("-----------------insert Test------------------")
DLL2 = dnodemngt(0)
for i in range(1, 11):
    DLL2.add(i)

DLL2.display()

DLL2.insert_before(1.5, 2)
DLL2.display()

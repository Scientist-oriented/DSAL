class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Nodecon:
    def __init__(self, data):
        self.head = Node(data)

    def add(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def delete(self, data):
        if self.head.data == data:
            temp = self.head
            self.head = self.head.next
            del temp
       
        else:
            node = self.head
            while node.next.data != data:
                node = node.next
            temp = node.next
            node.next = node.next.next
            temp.next = None
            del temp

    def display(self):
        if self.head == None:
            print("Nothing in the Linked List")

        else:
            node = self.head
            while node:
                print(node.data)
                node = node.next

    def search_node(self, data):
        node = self.head
        while True:
            if node.data == data:
                print("Found data: " + str(node.data))
                break
            elif node.next == None:
                print("No data in the list")
                break
            else:
                node = node.next

list = Nodecon(1)

for i in range(2, 10):
    list.add(i)

list.delete(5)

list.display()

list.search_node(11)

class Dnode:
    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

class Dnodecon:
    def __init__(self, data):
        self.head = Dnode(data)
        self.tail = self.head

    def add(self, data):
        if self.head == None:
            self.head = Dnode(data)
            self.tail = self.head
        else:
            temp = self.tail
            self.tail = Dnode(data)
            temp.next = self.tail
            self.tail.prev = temp
            del temp

    def display(self):
        node = self.head
        while node != None:
            print(node.data)
            node = node.next

    def Rdisplay(self):
        node = self.tail
        while node != None:
            print(node.data)
            node = node.prev

    def head_search(self, data):
        node = self.head
        while True:
            if node.data == data:
                print(str(node.data) + " Found in the List")
                return
            elif node.next == None:
                print("No data in the double list")
                return
            else:
                node = node.next
  
    def tail_search(self, data):
        node = self.tail
        while True:
            if node.data == data:
                print(str(node.data) + " Found in the List")
                return
            elif node.prev == None:
                print("No data in the double list")
                return
            else:
                node = node.prev
    
    def before_add(self, data, before):
        node = self.tail
        while True:
            if self.head.data == before:
                temp = self.head
                self.head = Dnode(data)
                temp.prev = self.head
                self.head.next = temp
                del temp
                return
            elif node.data == before:
                new = Dnode(data)
                new.prev = node.prev
                new.next = node
                new.prev.next = new
                node.prev = new
                return
            elif node.prev == None:
                print("No before_data in the list, Cannot add data")
                return
            else:
                node = node.prev

    def after_add(self, data, after):
        node = self.head
        while True:
            if self.tail.data == after:
                temp = self.tail
                self.tail = Dnode(data)
                self.tail.prev = temp
                temp.next = self.tail
                return
            elif node.data == after:
                new = Dnode(data)
                new.prev = node
                new.next = node.next
                node.next = new
                node.next.prev = new
                return
            elif node.next == None:
                print("No after_data in the list, Cannot add data")
                return
            else:
                node = node.next

    def delete(self, data):
        node = self.head
        while True:
            if self.head.data == data:
                temp = self.head
                self.head = self.head.next
                self.head.prev = None
                temp.next = None
                del temp
                return
            elif self.tail.data == data:
                temp = self.tail
                self.tail = self.tail.prev
                self.tail.next = None
                temp.prev = None
                return
            elif node.data == data:
                node.prev.next = node.next
                node.next.prev = node.prev
                node.prev = None
                node.next = None
                return
            else: 
                node = node.next
        

print("------------------Double----------------------")

Dlist = Dnodecon(1)

for i in range(2, 11):
    Dlist.add(i)

Dlist.display()

Dlist.head_search(15)
Dlist.tail_search(-1)
Dlist.before_add(0.5, 1)
Dlist.after_add(10.5, 10)

Dlist.display()
print("--------------------------------------------")
Dlist.Rdisplay()

print("--------------------------------------------")

Dlist.delete(3)
Dlist.delete(0.5)
Dlist.delete(10.5)
Dlist.display()
print("<reversed>")
Dlist.Rdisplay()

print("-----------------Hash-------------------")

import hashlib

hash_table = [0 for i in range(0, 3)]


def hash_key(data):
    byte_data = data.encode()
    hash_object = hashlib.sha256()
    hash_object.update(byte_data)
    hex_dig = hash_object.hexdigest()
    return int(hex_dig, 16)

def hash_address(key):
    return key % 3

def save_data(data, value):
    key = hash_key(data)
    address = hash_address(key)
    if hash_table[address] != 0:
        for i in range(0, len(hash_table[address])):
            if hash_table[address][i][0] == key:
                hash_table[address][i][1] = value
                return
        hash_table[address].append([key, value])
    else:
        hash_table[address] = [[key, value]]

print(hash_table)


print(hash_address(hash_key("Andy")))
print(hash_address(hash_key("Dave")))
print(hash_address(hash_key("Cathy")))

save_data("Andy", "English")
save_data("Dave", "Math")
save_data("Cathy", "Korean")

print(hash_table)
# 해쉬테이블
"""
hash_table = [0 for i in range(10)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 10

def save_data(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        hash_table[address] = [[key, value]]

    else:
        for index in range(len(hash_table[address])):
            if hash_table[address][index][0] == key:
                hash_table[address][index][1] = value
                return
        
        hash_table[address].append([key, value])
            


def read_data(data):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        print("No data in the list")

    else:
        for index in range(len(hash_table[address])):
            if hash_table[address][index][0] == key:
                print(hash_table[address][index][1])
                return
        print("No data in the list")
        

save_data("KIm", "Korea")
save_data("Johnson", "USA")
save_data("Yamamoto", "Japan")

print(hash_table)

read_data("KIm")
read_data("Johnson")
read_data("Yamamoto")

# linear probing

hash_table = [0 for i in range(10)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 10

def save_data(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] != 0:
        for index in range(address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return

    else:
        hash_table[address] = [key, value]

def read_data(data):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] != 0:
        for index in range(address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == key:
                return hash_table[address][1]
    else:
        return None

save_data("KIm", "Korea")
save_data("Johnson", "USA")
save_data("Yamamoto", "Japan")

print(hash_table)

a = read_data("KIm")
b = read_data("Johnson")
c = read_data("Yamamoto")

print(a)
print(b)
print(c)




# binary search tree

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class Nodecon:
    def __init__(self, head):
        self.head = head

    def insert(self, value):
        self.current_node = self.head

        while True:
            if value < self.current_node.value:
                if self.current_node.left != None:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right != None:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value):
        self.current_node = self.head

        while self.current_node:
            if value == self.current_node.value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right

        return False

    def delete(self, value):
        searched = False
        self.current_node = self.head
        self.parent_node = self.head

        while self.current_node:
            if value == self.current_node.value:
                searched = True
                break
            elif value < self.current_node.value:
                self.parent_node = self.current_node
                self.current_node = self.current_node.left
            else:
                self.parent_node = self.current_node
                self.current_node = self.current_node.right

        if searched == False:
            return False

        if self.current_node.left == None and self.current_node.right == None:
            if value < self.parent_node.value:
                self.parent_node.left = None
            else:
                self.parent_node.right = None

        elif self.current_node.left != None and self.current_node.right == None:
            if value < self.parent_node.value:
                self.parent_node.left = self.current_node.left
            else:
                self.parent_node.right = self.current_node.left

        elif self.current_node.left == None and self.current_node.right != None:
            if value < self.parent_node.value:
                self.parent_node.left = self.current_node.right
            else:
                self.parent_node.right = self.current_node.right

        else:
            if value < self.parent_node.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent_node.left = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

            else:
                self.change_node = self.current_node.right
                self.change_node_parent = self.current_node.right
                while self.change_node.left != None:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right != None:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent_node.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right

import random

bst_nums = set()
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))

head = Node(500)
binary_tree = Nodecon(head)
for num in bst_nums:
    binary_tree.insert(num)
    
for num in bst_nums:
    if binary_tree.search(num) == False:
        print ('search failed', num)

delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)


# 힙정렬 연습 (Max Heap)

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
            # 인덱스 번호 계산을 용이하게 하기 위해서 0번 인덱스는 None으로 채움
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx//2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]

            inserted_idx = parent_idx

        return True

    def move_down(self, popped_idx):
        left_child_idx = popped_idx * 2
        right_child_idx = popped_idx * 2 + 1

        if left_child_idx >= len(self.heap_array):
            return False

        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[left_child_idx] > self.heap_array[popped_idx]:
                return True
            else:
                return False

        else:
            if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                if self.heap_array[left_child_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return False

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_idx = popped_idx * 2
            right_child_idx = popped_idx * 2 + 1

            # 어차피 left child도 없으면 False로 반복문이 돌지 않으므로 여기에 쓸 필요 없음
            
            if right_child_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_idx

            else:
                if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                    if self.heap_array[left_child_idx] > self.heap_array[popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_idx
                    # 여기도 else가 필요없는 이유는 이미 move_down 함수에도 False처리 되었기 때문                     
                else:
                    if self.heap_array[right_child_idx] > self.heap_array[popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_idx] = self.heap_array[right_child_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_idx
                        
        return returned_data


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
a = heap.pop()
print(a)

print(heap.heap_array)



# 버블정렬 연습

def bubble_sort(data):
    for index in range(len(data)-1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False:
            break

    return data

import random

data_list = random.sample(range(100), 50)
print (bubble_sort(data_list))

# 선택정렬 연습

def selection_sort(data):
    for stand in range(len(data)-1):
        lowest = stand
        for index in range(stand+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data

data_list = random.sample(range(100), 10)
print(selection_sort(data_list))

# 삽입정렬 연습

def insert_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1, 0, -1):
            if data[index2] > data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break

    return data

data_list = random.sample(range(100), 10)
print(selection_sort(data_list))

# 재귀함수 연습

# 팩토리얼 구하는 함수

def factorial(num):
    if num <=1:
        return num
    else:
        return num * factorial(num - 1)

a = factorial(5)
print(a)

# 리스트의 총합을 구하는 함수

def list_sum(list):
    if len(list) == 1:
        return list[0]

    else:
        return list[0] + list_sum(list[1:])

list = [1,2,3,4,5,6,7,8,9,10]

b = list_sum(list)
print(b)

# string이 회문인지 알려주는 함수

def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

c = palindrome("motor")
d = palindrome("level")

print(c)
print(d)

def function(num):
    print(num)
    if num == 1:
        return

    if num % 2 == 1:
        return function(3*num+1)
    else:
        return function(int(num/2))


function(3)

def function2(num):
    if num == 1:
        return 1
    if num == 2:
        return 2
    if num == 3:
        return 4

    return function2(num-3) + function2(num-2) + function2(num-1)
    
e = function2(5)
print(e)


# 동적계획법 연습

def fibo(num):
    cache = [0 for index in range(num+1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num+1):
        cache[index] = cache[index-2] + cache[index-1]

    return cache[num]

a = fibo(100)
print(a)



# 링크드 리스트 연습

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeCon:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)

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
            print("No data in the List")
            return

        if self.head.data == data:
            self.head = self.head.next
            return
            
        node = self.head
        while node.next.data != data:
            node = node.next

        node.next = node.next.next
        return

    def search(self, data):
        node = self.head
        while node.next:
            if node.data == data:
                print("Data Found in the List")
                return
            else:
                node = node.next
        print("Data Not Found in the List")


L_list = NodeCon(1)

for i in range(2, 11):
    L_list.insert(i)

L_list.display()
L_list.delete(10)
L_list.display()
L_list.search(1)
L_list.search(3)
L_list.search(10)

# 더블 링크드 리스트 연습

class D_Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class D_NodeCon:
    def __init__(self, data):
        self.head = D_Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = D_Node(data)
            self.tail = D_Node(data)

        node = self.head
        while node.next:
            node = node.next

        new = D_Node(data)
        node.next = new
        new.prev = node
        self.tail = new

    def display_from_top(self):
        print("<Display from top>")
        node = self.head

        while node:
            print(node.data)
            node = node.next

    def display_from_bottom(self):
        print("<Display from bottom>")
        node = self.tail

        while node:
            print(node.data)
            node = node.prev

    def insert_before(self, data, before):
        if self.head == None:
            self.head = D_Node(data)
            self.tail = self.head
            print("Data Added in the Empty List")

        elif self.head.data == before:
            temp = self.head
            self.head = D_Node(data)
            self.head.next = temp
            temp.prev = self.head
            del temp

        else:
            node = self.tail
            while node.data != before:
                node = node.prev
                if node == None:
                    print("Failed to Find Before Data")
                    return

            new = D_Node(data)
            node.prev.next = new
            new.prev = node.prev
            new.next = node
            node.prev = new

    def insert_after(self, data, after):
        if self.head == None:
            self.head = D_Node(data)
            self.tail = self.head
            print("Data Added in the Empty List")

        elif self.tail.data == after:
            temp = self.tail
            self.tail = D_Node(data)
            temp.next = self.tail
            self.tail.prev = temp
            del temp

        else:
            node = self.head
            while node.data != after:
                node = node.next
                if node == None:
                    print("Failed to Find After Data")
                    return

            new = D_Node(data)
            node.next.prev = new
            new.next = node.next
            new.prev = node
            node.next = new




DL_List = D_NodeCon(1)
for i in range(2, 11):
    DL_List.insert(i)

DL_List.display_from_top()
# DL_List.display_from_bottom()

DL_List.insert_before(0.5, 1)
DL_List.insert_before(2.5, 3)
DL_List.insert_before(9.5, 10)
DL_List.display_from_top()

DL_List.insert_after(1.5, 1)
DL_List.insert_after(3.5, 3)
DL_List.insert_after(10.5, 10)
DL_List.display_from_top()
DL_List.display_from_bottom()



# 이진탐색 연습

def binary_search(data, search):
    if len(data) == 1 and data[0] == search:
        return True
    
    if len(data) == 1 and data[0] != search:
        return False

    if len(data) == 0:
        return False

    medium = len(data) // 2

    if data[medium] == search:
        return True
    else:
        if data[medium] > search:
            return binary_search(data[:medium], search)
        else:
            return binary_search(data[medium+1:], search)

import random
data_list = random.sample(range(10), 5)
data_list.sort()
print(data_list)
a = binary_search(data_list, 3)
print(a)

total_count = 0
check_count = 0
function_count = 0

# 이진 탐색을 검증하는 코드

while total_count != 100:
    data_list = random.sample(range(10), 5)
    data_list.sort()


    if 3 in data_list:
        check_count += 1

    if binary_search(data_list, 3) == True:
        function_count += 1

    total_count += 1

print(total_count)
print(check_count)
print(function_count)



# 순차탐색 연습

def sequential(data_list, search):
    for index in range(len(data_list)):
        if data_list[index] == search:
            return index

    return -1

import random

data_list = random.sample(range(10), 5)
print(data_list)

a = sequential(data_list, 3)
print(a)



# 해쉬테이블 chaining 복습

hash_table = [0 for i in range(5)]
print(hash_table)

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 5

def save_data(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        hash_table[address] = [[key, value]]

    else:
        for index in range(len(hash_table[address])):
            if hash_table[address][index][0] == key:
                hash_table[address][index][1] = value
                return
        hash_table[address].append([key, value])

def read_data(data):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        return False
    else:
        for index in range(len(hash_table[address])):
            if hash_table[address][index][0] == key:
                return hash_table[address][index][1]
        return False

save_data("Kim", "Korean")
save_data("Lee", "History")
save_data("Moon", "English")

a = read_data("Kim")
b = read_data("Lee")
c = read_data("Moon")

print(hash_table)

print(a, b, c)



# hash_table linear probing 기법

hash_table = [0 for i in range(3)]
print(hash_table)

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 3

def show_address(data):
    print(hash(data) % 3)

def save_data(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        hash_table[address] = [key, value]

    else:
        for index in range(address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return
        for index in range(0, address):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return
        print("Full table")


save_data("Kim", "Korean")
save_data("Lee", "History")
save_data("Moon", "English")
save_data("Park", "Social Studies")

show_address("Kim")
show_address("Lee")
show_address("Moon")



print(hash_table)


# 이진탐색 연습

def binary_search(data_list, search):
    if len(data_list) == 1 and data_list[0] == search:
        return True
    
    if len(data_list) == 1 and data_list[0] != search:
        return False

    if len(data_list) == 0:
        return False

    medium = len(data_list) // 2

    if data_list[medium] == search:
        return True
    elif data_list[medium] > search:
        return binary_search(data_list[:medium], search)
    else:
        return binary_search(data_list[medium+1:], search)

import random
data_list = random.sample(range(10), 5)
data_list.sort()
print(data_list)
a = binary_search(data_list, 3)
print(a)

count1 = 0
count2 = 0
total_count = 0

while total_count != 100:
    data_list = random.sample(range(10), 5)
    data_list.sort()

    if 3 in data_list:
        count1 += 1

    if binary_search(data_list, 3) == True:
        count2 += 1

    total_count += 1

print(count1)
print(count2)


# 순차탐색 연습

def sequential(data_list, search):
    for index in range(len(data_list)):
        if data_list[index] == search:
            return index
    return -1

import random

data_list = random.sample(range(10), 5)
print(data_list)

a = sequential(data_list, 3)
print(a)


# 넓이우선탐색 연습

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

a = bfs(graph, "A")
print(a)



# 깊이우선탐색

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph, start_node):
    visited = []
    need_visit = []

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()

        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

a = dfs(graph, "A")
print(a)


# 탐욕알고리즘: 동전문제 연습

coin_list = [1, 100, 50, 500]

def min_coin_count(value, coin_list):
    coin_list.sort(reverse=True)
    total_coin_count = 0
    details = list()

    for coin in coin_list:
        coin_count = value // coin
        total_coin_count += coin_count
        value -= coin * coin_count
        details.append([coin, coin_count])

    return total_coin_count, details

a = min_coin_count(7777, coin_list)
print(a)


# 이진탐색트리

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class NodeCon:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            node = self.head
            while True:
                if data < node.data:
                    if node.left == None:
                        node.left = Node(data)
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = Node(data)
                        break
                    else:
                        node = node.right

    def search(self, data):
        node = self.head

        while node:
            if node.data == data:
                return True
            elif node.data > data:
                node = node.left
            else:
                node = node.right

        return False

    def delete(self, data):
        searched = False
        node = self.head
        parent_node = self.head

        while node:
            if node.data == data:
                searched = True
                break
            elif node.data > data:
                parent_node = node
                node = node.left
            else:
                parent_node = node
                node = node.right

        if searched == False:
            return False

        if node.left == None and node.right == None:
            if data < parent_node.data:
                parent_node.left = None
            else:
                parent_node.right = None

        elif node.left != None and node.right == None:
            if data < parent_node.data:
                parent_node.left = node.left
            else:
                parent_node.right = node.left

        elif node.left == None and node.right != None:
            if data < parent_node.data:
                parent_node.left = node.right
            else:
                parent_node.right = node.right

        else:
            change_node = node.right
            change_node_parent = node.right
            while change_node.left:
                change_node_parent = change_node
                change_node = change_node.left
            if change_node.right != None:
                change_node_parent.left = change_node.right
            else:
                change_node_parent.left = None

            if data < parent_node.data:
                parent_node.left = change_node
                change_node.left = node.left
                change_node.right = node.right
            else:
                parent_node.right = change_node
                change_node.left = node.left
                change_node.right = node.right

import random

nums = set()
while len(nums) != 10:
    nums.add(random.randint(0, 99))

print(nums)

tree = NodeCon(50)
for node in nums:
    tree.insert(node)

nums = list(nums)
del_nums = set()
while len(del_nums) != 2:
    del_nums.add(nums[random.randint(0, 9)])

for node in del_nums:
    tree.delete(node)



# 이진탐색 연습

def binary_search(data_list, data):
    if len(data_list) == 1 and data_list[0] == data:
        return True

    if len(data_list) == 1 and data_list[0] != data:
        return False

    if len(data_list) == 0:
        return False

    medium = len(data_list) // 2

    if data_list[medium] == data:
        return True
    elif data_list[medium] > data:
        return binary_search(data_list[:medium], data)
    else:
        return binary_search(data_list[medium+1:], data)


import random
data_list = random.sample(range(10), 5)
data_list
data_list.sort()
print(data_list)
a = binary_search(data_list, 3)
print(a)

# 순차탐색연습

def sequential(data_list, data):
    for index in range(len(data_list)):
        if data_list[index] == data:
            return index
    return -1

import random
data_list = random.sample(range(10), 5)
data_list
print(data_list)
a = sequential(data_list, 3)
print(a)




# 너비우선탐색

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start_node):
    visited = []
    need_visit = []
    
    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

a = bfs(graph, "A")
print(a)

# 깊이우선탐색

def dfs(graph, start_node):
    visited = list()
    need_visit = list()

    need_visit.append(start_node)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

b = dfs(graph, "A")
print(b)



# 탐욕알고리즘(동전문제) 연습

coin_list = [1, 200, 50, 500]


def min_coin_count(coin_list, value):
    total_coin_count = 0
    details = list()
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_count = value // coin
        value -= coin_count * coin
        total_coin_count += coin_count
        details.append([coin, coin_count])

    return total_coin_count, details

a = min_coin_count(coin_list, 4720)
print(a)

# 탐욕알고리즘(부분 배낭 문제) 연습

data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def max_value(data_list, capacity):
    data_list = sorted(data_list, key= lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity >= data[0]:
            capacity -= data[0]
            total_value += data[1]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += fraction * data[1]
            details.append([data[0], data[1], fraction])
            break
    return total_value, details

b = max_value(data_list, 30)
print(b)


# 힙 연습

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True
        
        self.heap_array.append(data)
        inserted_index = len(self.heap_array) - 1

        while self.move_up(inserted_index):
            parent_index = inserted_index // 2
            self.heap_array[inserted_index], self.heap_array[parent_index] = self.heap_array[parent_index], self.heap_array[inserted_index]
            inserted_index = parent_index

        return True

    def move_up(self, inserted_index):
        if inserted_index <= 1:
            return False

        parent_index = inserted_index // 2

        if self.heap_array[parent_index] < self.heap_array[inserted_index]:
            return True
        else:
            return False
        
    def pop(self):
        if len(self.heap_array) <= 1:
            return False
        
        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_idx = 2 * popped_idx
            right_child_idx = 2 * popped_idx + 1

            if right_child_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_idx
            else:
                if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                    if self.heap_array[left_child_idx] > self.heap_array[popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_idx
                else:
                    if self.heap_array[right_child_idx] > self.heap_array[popped_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_idx] = self.heap_array[right_child_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_idx

        return returned_data
                  

    def move_down(self, popped_idx):
        left_child_idx = 2 * popped_idx
        right_child_idx = 2 * popped_idx + 1

        if left_child_idx >= len(self.heap_array):
            return False
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                if self.heap_array[left_child_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

a = heap.pop()
print(a)

print(heap.heap_array)



# 힙 연습

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            if self.heap_array[parent_idx] < self.heap_array[inserted_idx]:
                self.heap_array[parent_idx], self.heap_array[inserted_idx] = self.heap_array[inserted_idx], self.heap_array[parent_idx]
                inserted_idx = parent_idx

        return True


    def move_up(self, inserted_idx):
        if inserted_idx == 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[parent_idx] < self.heap_array[inserted_idx]:
            return True
        else:
            return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return False

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_idx = popped_idx * 2
            right_child_idx = popped_idx * 2 + 1

            
            if right_child_idx >= len(self.heap_array):
                if self.heap_array[left_child_idx] > self.heap_array[popped_idx]:
                    self.heap_array[left_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_idx]
                    popped_idx = left_child_idx
            else:
                if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                    if self.heap_array[left_child_idx] > self.heap_array[popped_idx]:
                        self.heap_array[left_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_idx]
                        popped_idx = left_child_idx                
                else:
                    if self.heap_array[right_child_idx] > self.heap_array[popped_idx]:
                        self.heap_array[right_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[right_child_idx]
                        popped_idx = right_child_idx
                        

        return returned_data
                
    
    def move_down(self, popped_idx):
        left_child_idx = popped_idx * 2
        right_child_idx = popped_idx * 2 + 1

        if left_child_idx >= len(self.heap_array):
            return False
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[left_child_idx] > self.heap_array[popped_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_idx] > self.heap_array[right_child_idx]:
                if self.heap_array[left_child_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_idx] > self.heap_array[popped_idx]:
                    return True
                else:
                    return False
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

a = heap.pop()
print(a)

print(heap.heap_array)


# 버블정렬

def bubble_sort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False:
            break
    return True

import random

data_list = random.sample(range(100), 50)
print(data_list)
bubble_sort(data_list)
print(data_list)

# 삽입정렬

def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return True

data_list = random.sample(range(100), 50)
print(data_list)
insertion_sort(data_list)
print(data_list)

# 선택정렬

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return True

data_list = random.sample(range(100), 50)
print(data_list)
selection_sort(data_list)
print(data_list)



# 너비우선탐색

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start):
    visited = []
    need_visit = []
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

a = bfs(graph, "A")
print(a)

# 깊이우선탐색

def dfs(graph, start):
    visited = []
    need_visit = []

    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

b = dfs(graph, "A")
print(b)

# 탐욕알고리즘 동전문제 연습

coin_list = [1, 100, 50, 500]

def min_coin_count(coin_list, value):
    total_coin_count = 0
    details = []
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_count = value // coin
        total_coin_count += coin_count
        value -= coin * coin_count
        details.append([coin, coin_count])

    return total_coin_count, details

c = min_coin_count(coin_list, 4720)
print(c)

# 탐욕알고리즘 가방문제 연습

data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def get_max_value(data_list, capacity):
    total_value = 0
    details = []
    data_list = sorted(data_list, key= lambda x: x[1] / x[0], reverse=True)

    for data in data_list:
        if data[0] <= capacity:
            total_value += data[1]
            capacity -= data[0]
            details.append([data[1], data[0], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[1], data[0], fraction])
            break

    return total_value, details

d = get_max_value(data_list, 30)
print(d)


# 해쉬테이블 chaining 연습

hash_table = [0 for i in range(5)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 5

def save_data(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        hash_table[address] = [[key, value]]
    else:
        for index in range(len(hash_table[address])):
            if hash_table[address][index][0] == key:
                hash_table[address][index][1] = value
                return
        hash_table[address].append([key, value])

def read_data(data):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        return False
    else:
        for index in range(len(hash_table[address])):
            if hash_table[address][index][0] == key:
                return hash_table[address][index][1]
        return False

save_data("Kim", "Korean")
save_data("Lee", "History")
save_data("Moon", "English")
save_data("Park", "Social Studies")


a = read_data("Kim")
b = read_data("Lee")
c = read_data("Moon")
d = read_data("Park")
print(a, b, c, d)
print(hash_table)


# 해쉬테이블 linear probing 기법

hash_table = [0 for i in range(5)]

def get_key(data):
    return hash(data)

def hash_function(key):
    return key % 5

def save_data(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] != 0:
        for index in range(address, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return
            
        for index in range(0, address):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return 
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return
            
    else:
        hash_table[address] = [key, value]

def show_address(data):
    print(data + ":" + str(hash(data) % 5))

def read_data(data):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] != 0:
        for index in range(address, len(hash_table)):
            if hash_table[index] == 0:
                return None
            elif hash_table[index][0] == key:
                return hash_table[index][1]
        
        for index in range(0, address):
            if hash_table[index] == 0:
                return None
            if hash_table[index][0] == key:
                return hash_table[index][1]
            
    else:
        return None

count = 0
save_error = 0
read_error = 0

while count != 1000:
    count +=1

    save_data("Kim", "K")
    save_data("Lee", "L")
    save_data("Moon", "M")
    save_data("Park", "P")
    save_data("Ahn", "A")


    a = read_data("Kim")
    b = read_data("Lee")
    c = read_data("Moon")
    d = read_data("Park")
    e = read_data("Ahn")

    if 0 in hash_table:
        save_error += 1

    if a == None or b== None or c == None or d == None or e == None:
        read_error += 1 

# show_address("Kim")
# show_address("Lee")
# show_address("Moon")
# show_address("Park")
# show_address("Ahn")
    
print(count)
print(save_error)
print(read_error)



# 트리 연습

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Nodecon:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        else:
            current_node = self.head
            while True:
                if data < current_node.data:
                    if current_node.left == None:
                        current_node.left = Node(data)
                        return
                    else:
                        current_node = current_node.left
                if data > current_node.data:
                    if current_node.right == None:
                        current_node.right = Node(data)
                        return
                    else:
                        current_node = current_node.right
    
    def search(self, data):
        current_node = self.head
        while current_node:
            if data == current_node.data:
                return True
            elif data < current_node.data:
                current_node = current_node.left
            else:
                current_node = current_node.right
        return False

    def delete(self, data):
        searched = False

        current_node = self.head
        parent_node = self.head

        while current_node:
            if data == current_node.data:
                searched = True
                break
            elif data < current_node.data:
                parent_node = current_node
                current_node = current_node.left
            else:
                parent_node = current_node
                current_node = current_node.right

        if searched == False:
            return False

        if current_node.left == None and current_node.right == None:
            if data < parent_node.data:
                parent_node.left = None
            else:
                parent_node.right = None

        elif current_node.left != None and current_node.right == None:
            if data < parent_node.data:
                parent_node.left = current_node.left
            else:
                parent_node.right = current_node.left

        elif current_node.left == None and current_node != None:
            if data < parent_node.data:
                parent_node.left = current_node.right
            else:
                parent_node.right = current_node.right

        else:
            change_node = current_node.right
            change_node_parent = current_node.right
            while change_node.left:
                change_node_parent = change_node
                change_node = change_node.left
            if change_node.right != None:
                change_node_parent.left = change_node.right
            else:
                change_node_parent.left = None
           
            if data < parent_node.data:
                parent_node.left = change_node
                change_node.left = current_node.left
                change_node.right = current_node.right
            else:
                parent_node.right = change_node
                change_node.left = current_node.left
                change_node.right = current_node.right


import random
# 0 ~ 999 중, 100 개의 숫자 랜덤 선택
bst_nums = set()
    # 중복되면 안되니까 중복을 제거해주는 set를 사용
while len(bst_nums) != 100:
    bst_nums.add(random.randint(0, 999))
# print (bst_nums)

# 선택된 100개의 숫자를 이진 탐색 트리에 입력, 임의로 루트노드는 500을 넣기로 함

binary_tree = Nodecon(500)
for num in bst_nums:
    binary_tree.insert(num)
    
# 입력한 100개의 숫자 검색 (검색 기능 확인)
for num in bst_nums:
    if binary_tree.search(num) == False:
        print ('search failed', num)

# 입력한 100개의 숫자 중 10개의 숫자를 랜덤 선택
delete_nums = set()
    # 중복되면 안되니까 set로
bst_nums = list(bst_nums)
while len(delete_nums) != 10:
    delete_nums.add(bst_nums[random.randint(0, 99)])

# 선택한 10개의 숫자를 삭제 (삭제 기능 확인)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)



# 버블정렬연습

def bubble_sort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False:
            break
    return data

import random

data_list = random.sample(range(100), 50)
print (bubble_sort(data_list))

# 삽입정렬 연습

def insert_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data

data_list = random.sample(range(100), 50)
print (insert_sort(data_list))

# 선택정렬 연습

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[stand], data[lowest] = data[lowest], data[stand]
    return data


data_list = random.sample(range(100), 50)
print (selection_sort(data_list))



# 버블정렬연습

def bubble_sort(data):
    for index in range(len(data) - 1):
        swap  = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False:
            break
    return data

import random

data_list = random.sample(range(100), 50)
print (bubble_sort(data_list))

# 삽입정렬연습

def insert_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
    return data

data_list = random.sample(range(100), 50)
print (insert_sort(data_list))

# 선택정렬

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data

data_list = random.sample(range(100), 50)
print (selection_sort(data_list))



# 탐욕알고리즘 가방문제 연습

data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def max_value(data_list, capacity):
    data = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = []

    for data in data_list:
        if data[0] < capacity:
            total_value += data[1]
            capacity -= data[0]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append([data[0], data[1], fraction])
            break
    return total_value, details

a = max_value(data_list, 30)

print(a)
            


# 다익스트라 알고리즘 복습

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

print(dijkstra(mygraph, "A"))



# 다익스트라 알고리즘 연습

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = weight + current_distance

            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

print(dijkstra(mygraph, 'A'))



# 크루스칼 알고리즘 연습

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()

    for node in graph['vertices']:
        make_set(node)

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst

print(kruskal(mygraph))



# 크루스칼 알고리즘 연습

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()

    for node in graph["vertices"]:
        make_set(node)

    edges = graph['edges']
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge

        if find(node_u) != find(node_v):
            union(node_u, node_v)
            mst.append(edge)

    return mst

print(kruskal(mygraph))



# 힙 연습 (최소힙)

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2

        if self.heap_array[parent_idx] > self.heap_array[inserted_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[parent_idx], self.heap_array[inserted_idx] = self.heap_array[inserted_idx], self.heap_array[parent_idx]
            inserted_idx = parent_idx

        return True

    def move_down(self, popped_idx):
        left_child_idx = 2 * popped_idx
        right_child_idx = 2 * popped_idx + 1

        if left_child_idx >= len(self.heap_array):
            return False
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] > self.heap_array[left_child_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                if self.heap_array[popped_idx] > self.heap_array[left_child_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_idx] > self.heap_array[right_child_idx]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return False

        returned_data = self.heap_array[1]
        self.heap_array[1], self.heap_array[-1] = self.heap_array[-1], self.heap_array[1]
        del self.heap_array[-1]
        popped_idx = 1

        

        while self.move_down(popped_idx):
            left_child_idx = 2 * popped_idx
            right_child_idx = 2 * popped_idx + 1

            if right_child_idx >= len(self.heap_array):
                if self.heap_array[popped_idx] > self.heap_array[left_child_idx]:
                    self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                    popped_idx = left_child_idx
            else:
                if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                    if self.heap_array[popped_idx] > self.heap_array[left_child_idx]:
                        self.heap_array[popped_idx], self.heap_array[left_child_idx] = self.heap_array[left_child_idx], self.heap_array[popped_idx]
                        popped_idx = left_child_idx
                else:
                    if self.heap_array[popped_idx] > self.heap_array[right_child_idx]:
                        self.heap_array[popped_idx], self.heap_array[right_child_idx] = self.heap_array[right_child_idx], self.heap_array[popped_idx]
                        popped_idx = right_child_idx

        return returned_data
                    
heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

a = heap.pop()
print(a)

print(heap.heap_array)
b = heap.pop()
print(b)
print(heap.heap_array)

heap.insert(1)
c = heap.heap_array
print(c)



# 링크드 리스트 연습

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeCon:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            return 

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
            return False

        if data == self.head.data:
            self.head = self.head.next
        
        else:
            node = self.head

            while node.next.data != data:
                node = node.next

            node.next = node.next.next

        return

    def search(self, data):
        node = self.head
        while node.next:
            if node.data == data:
                return True
            else:
                node = node.next

        return False
            

List = NodeCon(1)

for index in range(2, 11):
    List.insert(index)

List.display()

for index in [3, 6, 9]:
    List.delete(index)

List.display()



# 더블링크드 리스트 연습

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class NodeCon:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        
        else:
            temp = self.tail
            self.tail = Node(data)
            temp.next = self.tail
            self.tail.prev = temp
            del temp
    
    def display(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def insert_before(self, data, before):
        if before == self.head.data:
            new = Node(data)
            self.head.prev = new
            new.next = self.head
            self.head = new
        else:
            before_node = self.tail
            while before_node.data != before:
                before_node = before_node.prev
                if before_node == None:
                    return False

            new = Node(data)

            before_new = before_node.prev
            before_new.next = new
            new.prev = before_node.prev
            new.next = before_node
            before_new = new

    def insert_after(self, data, after):
        if after == self.tail.data:
            new = Node(data)
            self.tail.next = new
            new.prev = self.tail
            self.tail = new

        else:
            after_node = self.head
            while after_node.data != after:
                after_node = after_node.next
                if after_node == None:
                    return False

            new = Node(data)
            after_new = after_node.next

            after_node.next = new
            new.prev = after_node
            new.next = after_new
            after_new.prev = new
    
    def delete(self, data):
        if data == self.head.data:
            self.head = self.head.next
            self.head.prev = None

        elif data == self.tail.data:
            self.tail = self.tail.prev
            self.tail.next = None

        else:
            before_node = self.head
            while before_node.next.data != data:
                before_node = before_node.next
                if before_node.next == None:
                    return False

            after_node = before_node.next.next
            before_node.next = after_node
            after_node.prev = before_node
        


List = NodeCon(1)

for index in range(2, 11):
    List.insert(index)

List.display()

List.insert_before(0.5, 1)
List.insert_before(3.5, 4)
List.insert_after(4.5, 4)
List.insert_after(10.5, 10)
List.display()
print("Head: " + str(List.head.data))
print("Tail: " + str(List.tail.data))

List.delete(0.5)
List.delete(10.5)
List.delete(3.5)
List.delete(4.5)
List.display()

print("Head: " + str(List.head.data))
print("Tail: " + str(List.tail.data))



# 병합정렬 연습

def merge_sort(data):
    if len(data) <= 1:
        return data
    
    medium = int(len(data) // 2)

    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])

    return merge(left, right)

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] < right[right_point]:
            merged.append(left[left_point])
            left_point += 1
        else:
            merged.append(right[right_point])
            right_point += 1

    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

import random

data_list = random.sample(range(100), 10)
a = merge_sort(data_list)
print(a)



# 병합정렬 연습

def merge_sort(data):
    if len(data) <= 1:
        return data

    medium = int(len(data)//2)

    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])

    return merge(left, right)

def merge(left, right):
    merged = list()
    left_point, right_point = 0, 0

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] < right[right_point]:
            merged.append(left[left_point])
            left_point += 1
        else:
            merged.append(right[right_point])
            right_point += 1

    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

    
import random

data_list = random.sample(range(100), 10)
a = merge_sort(data_list)
print(a)



# 퀵정렬

def qsort(data):
    if len(data) <= 1:
        return data

    left, right = list(), list()
    pivot = data[0]

    for index in range(1, len(data)):
        if pivot > data[index]:
            left.append(data[index])
        else:
            right.append(data[index])

    return qsort(left) + [pivot] + qsort(right)



def qsort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item >= pivot]

    return qsort(left) + [pivot] + qsort(right)

import random

data_list = random.sample(range(100), 10)

a = qsort(data_list)
print(a)



# 재귀함수 팩토리얼

def factorial(num):
    if num <= 1:
        return num

    return num * factorial(num - 1)

a = factorial(5)
print(a)



# 재귀함수 리스트의 합

def list_sum(list):
    if len(list) <= 1:
        return list[0]

    return list[0] + list_sum(list[1:])

list = [1, 2, 3]
a = list_sum(list)
print(a)



# 재귀함수 회문

def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

a = palindrome("motor")
b = palindrome("level")
print(a, b)



# 재귀함수 짝수홀수

def func(n):
    if n == 1:
        print(n)
        return

    if n % 2 == 1:
        print(n)
        return func(3 * n + 1)

    if n % 2 == 0:
        print(n)
        return func(int(n/2))

func(3)


# 동적프로그래밍

def fibo(num):
    cache = [0 for i in range(num+1)]

    cache[0] = 0
    cache[1] = 1

    for index in range(2, num+1):
        cache[index] = cache[index - 2] + cache[index - 1]

    return cache[num]

a = fibo(10)
print(a)



# 순차탐색

def sequential(data_list, data):
    for index in range(len(data_list)):
        if data_list[index] == data:
            return index
    return -1

import random

data_list = list()
for num in range(10):
    data_list.append(random.randint(1, 100))

print(data_list)
a = sequential(data_list, 20)
print(a)



# 이진탐색

def binary_search(data, search):
    if len(data) == 1 and data[0] == search:
        return True
    if len(data) == 1 and data[0] != search:
        return False
    if len(data) == 0:
        return False

    medium = len(data) // 2

    if data[medium] == search:
        return True
    elif data[medium] > search:
        return binary_search(data[:medium], search)
    else:
        return binary_search(data[medium+1:], search)


import random
data_list = random.sample(range(10), 5)
data_list.sort()

print(data_list)
a = binary_search(data_list, 3)
print(a)



# BFS 연습

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start):
    need_visit = []
    visited = []
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

a = bfs(graph, "A")
print(a)



# 깊이우선탐색 연습

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph, start):
    visited = []
    need_visit = []
    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    
    return visited

a = dfs(graph, "A")
print(a)



# 그리디 알고리즘 동전문제

coin_list = [500, 50, 100, 1]

def min_coin_count(coin_list, value):
    total_coin_count = 0
    details = []
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_count = value // coin
        total_coin_count += coin_count
        value -= coin * coin_count
        details.append([coin, coin_count])

    return total_coin_count, details

a = min_coin_count(coin_list, 4720)
print(a)

# 그리디 알고리즘 가방문제

data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def max_value(data_list, capacity):
    total_value = 0
    details = []
    data_list = sorted(data_list, key= lambda x : x[1] / x[0], reverse=True)

    for data in data_list:
        if capacity > data[0]:
            total_value += data[1]
            capacity -= data[0]
            details.append([data[0], data[1], 1])
        else:
            fraction = capacity / data[0]
            total_value += fraction * data[1]
            details.append([data[0], data[1], fraction])
            break
    
    return total_value, details

a = max_value(data_list, 30)
print(a)



# Dijkstra's Algorithm Practice

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def dijkstra(graph, start):

    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight

            if distances[adjacent] > distance:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

a = dijkstra(mygraph, "A")
print(a)



# 다익스트라 알고리즘
mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = [] 
    heapq.heappush(queue, [distances[start], start])

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distances[adjacent], adjacent])

    return distances

a = dijkstra(mygraph, "A")
print(a)



# 트리 연습

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Nodecon:
    def __init__(self, head):
        self.head = head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
        
        node = self.head
        while True:
            if node.data > data:
                if node.left == None:
                    node.left = Node(data)
                    break
                else:
                    node = node.left
            else:
                if node.right == None:
                    node.right = Node(data)
                    break
                else:
                    node = node.right

    def search(self, data):
        node = self.head

        while node:
            if node.data == data:
                return True
            elif node.data > data:
                node = node.left
            else:
                node = node.right

        return False

    def delete(self, data):
        searched = False

        node = self.head
        parent_node = self.head

        while node:
            if node.data == data:
                searched = True
                break
            elif node.data > data:
                parent_node = node
                node = node.left
            else:
                parent_node = node
                node = node.right

        if searched == False:
            return False
            
        if node.left == None and node.right == None:
            if parent_node.data > node.data:
                parent_node.left = None
            else:
                parent_node.right = None
        
        elif node.left != None and node.right == None:
            if parent_node.data > node.data:
                parent_node.left = node.left
            else:
                parent_node.right = node.left

        elif node.left == None and node.right != None:
            if parent_node.data > node.data:
                parent_node.left = node.right
            else:
                parent_node.right = node.right
            
        else:
            if parent_node.data > node.data:
                change_node = node.right
                change_node_parent = node.right
                while change_node.left:
                    change_node_parent = change_node
                    change_node = change_node.left
                if change_node.right == None:
                    change_node_parent.left = None
                else:
                    change_node_parent.left = change_node.right

                parent_node.left = change_node
                change_node.left = node.left
                change_node.right = node.right

            else:
                change_node = node.right
                change_node_parent = node.right
                while change_node.left:
                    change_node_parent = change_node
                    change_node = change_node.left
                if change_node.right == None:
                    change_node_parent.left = None
                else:
                    change_node_parent.left = change_node.right

                parent_node.right = change_node
                change_node.left = node.left
                change_node.right = node.right

        return True

import random

# bst_nums = set()

# while len(bst_nums) != 100:
#     bst_nums.add(random.randint(0, 999))

bst_nums = [1, 2, 3, 4, 6, 7, 8, 9, 10]
head = Node(5)
binary_tree = Nodecon(head)
for num in bst_nums:
    binary_tree.insert(num)

for num in bst_nums:
    if binary_tree.search(num) != False:
        print("Found", num)

delete_nums = set()
bst_nums = list(bst_nums)
while len(delete_nums) != 5:
    delete_nums.add(bst_nums[random.randint(0, 8)])

print(delete_nums)
delete_nums = list(delete_nums)
for del_num in delete_nums:
    if binary_tree.delete(del_num) == False:
        print('delete failed', del_num)
    else:
        print('delete successed', del_num)
# success_count = 0
# fail_count = 0
# for del_num in delete_nums:
#     if binary_tree.delete(del_num) != False:
#         success_count += 1
#     else:
#         fail_count += 1

# print(success_count, fail_count)


# 크루스칼 알고리즘

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()

    for node in graph["vertices"]:
        make_set(node)

    edges = graph["edges"]
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge
        if find(node_v) != find(node_u):
            union(node_v, node_u)
            mst.append(edge)

    return mst

a = kruskal(mygraph)
print(a)



# 크루스칼 알고리즘

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = []

    for node in graph["vertices"]:
        make_set(node)

    edges = graph["edges"]
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge

        if find(node_v) != find(node_u):
            union(node_u, node_v)
            mst.append(edge)

    return mst

a = kruskal(mygraph)
print(a)



# 최소 힙복습

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2

        if self.heap_array[inserted_idx] < self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
        else:
            self.heap_array.append(data)
            inserted_idx = len(self.heap_array) - 1

            while self.move_up(inserted_idx):
                parent_idx = inserted_idx // 2
                self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
                inserted_idx = parent_idx
                
    def pop(self):
        returned_data = self.heap_array[1]
        self.heap_array[1], self.heap_array[-1] = self.heap_array[-1], self.heap_array[1]
        del self.heap_array[-1]

        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_idx = 2 * popped_idx
            right_child_idx = 2 * popped_idx + 1

            
            if right_child_idx >= len(self.heap_array):
                if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                    self.heap_array[left_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_idx]
                    popped_idx = left_child_idx
            else:
                if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                    if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                        self.heap_array[left_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_idx]
                        popped_idx = left_child_idx
                else:
                    if self.heap_array[right_child_idx] < self.heap_array[popped_idx]:
                        self.heap_array[right_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[right_child_idx]
                        popped_idx = right_child_idx

        return returned_data

    def move_down(self, popped_idx):
        left_child_idx = 2 * popped_idx
        right_child_idx = 2 * popped_idx + 1

        if left_child_idx >= len(self.heap_array):
            return False
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_idx] < self.heap_array[popped_idx]:
                    return True
                else:
                    return False


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)



# 버블정렬

def bubble_sort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(0, len(data)-index-1):
            if data[index2 + 1] < data[index2]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False:
            break
    return data

import random

Testlist = random.sample(range(100), 50)
print(Testlist)

bubble_sort(Testlist)
print(Testlist)


# 삽입정렬

def insertion_sort(data):
    for index in range(0, len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data

import random

Testlist = random.sample(range(100), 50)
print(Testlist)

insertion_sort(Testlist)
print(Testlist)




# 선택정렬

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand+1, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[stand], data[lowest] = data[lowest], data[stand]
    return data

import random

Testlist = random.sample(range(100), 50)
print(Testlist)

selection_sort(Testlist)
print(Testlist)



# 병합정렬

def merge_sort(data):
    if len(data) <= 1:
        return data

    medium = int(len(data) / 2)
    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])

    return merge(left, right)

def merge(left, right):
    left_point = 0
    right_point = 0
    merged = []

    while len(left) > left_point and len(right) > right_point:
        if left[left_point] < right[right_point]:
            merged.append(left[left_point])
            left_point += 1
        else:
            merged.append(right[right_point])
            right_point += 1

    while len(left) > left_point:
        merged.append(left[left_point])
        left_point += 1

    while len(right) > right_point:
        merged.append(right[right_point])
        right_point += 1

    return merged

import random

Testlist = random.sample(range(100), 50)
print(Testlist)

a = merge_sort(Testlist)
print(a)



# 퀵소트

def quick_sort(data):
    if len(data) <= 1:
        return data

    left = []
    right = []
    pivot = data[0]

    for index in range(1, len(data)):
        if data[index] < pivot:
            left.append(data[index])
        else:
            right.append(data[index])

    return quick_sort(left) + [pivot] + quick_sort(right)

import random

Testlist = random.sample(range(100), 50)
print(Testlist)

a = quick_sort(Testlist)
print(a)

def qsort(data):
    if len(data) <= 1:
        return data
    
    pivot = data[0]
    left = [item for item in data[1:] if pivot > item]
    right = [item for item in data[1:] if pivot < item]

    return quick_sort(left) + [pivot] + quick_sort(right)

import random

Testlist = random.sample(range(100), 50)
print(Testlist)

b = qsort(Testlist)
print(b)



# 재귀함수 팩토리얼

def factorial(num):
    if num <= 1:
        return num

    return num * factorial(num - 1)

a = factorial(5)
print(a)

# 재귀함수 리스트의 합

def list_sum(data):
    if len(data) <= 1:
        return data[0]

    return data[0] + list_sum(data[1:])

# 재귀함수 회문

def palindrome(string):
    if len(string) <= 1:
        return True

    if string[0] == string[-1]:
        return palindrome(string[1:-1])
    else:
        return False

b = palindrome("Motor")
c = palindrome("level")
print(b, c)

# 동적계획법 피보나치 수열

def fibo(num):
    cache = [0 for i in range(num + 1)]
    cache[0] = 0
    cache[1] = 1

    for index in range(2, num+1):
        cache[index]  = cache[index-2] + cache[index-1]

    return cache[num]

d = fibo(10)
print(d)



# 링크드리스트 연습

# 크루스칼 알고리즘

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node_v, node_u):
    root1 = find(node_v)
    root2 = find(node_u)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = []

    for node in graph["vertices"]:
        make_set(node)

    edges = graph["edges"]
    edges.sort()

    for edge in edges:
        weight, node_v, node_u = edge

        if find(node_v) != find(node_u):
            union(node_u, node_v)
            mst.append(edge)

    return mst

a = kruskal(mygraph)
print(a)



# 최소 힙복습

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2

        if self.heap_array[inserted_idx] < self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(data)
        else:
            self.heap_array.append(data)
            inserted_idx = len(self.heap_array) - 1

            while self.move_up(inserted_idx):
                parent_idx = inserted_idx // 2
                self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
                inserted_idx = parent_idx
                
    def pop(self):
        returned_data = self.heap_array[1]
        self.heap_array[1], self.heap_array[-1] = self.heap_array[-1], self.heap_array[1]
        del self.heap_array[-1]

        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_idx = 2 * popped_idx
            right_child_idx = 2 * popped_idx + 1

            
            if right_child_idx >= len(self.heap_array):
                if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                    self.heap_array[left_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_idx]
                    popped_idx = left_child_idx
            else:
                if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                    if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                        self.heap_array[left_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[left_child_idx]
                        popped_idx = left_child_idx
                else:
                    if self.heap_array[right_child_idx] < self.heap_array[popped_idx]:
                        self.heap_array[right_child_idx], self.heap_array[popped_idx] = self.heap_array[popped_idx], self.heap_array[right_child_idx]
                        popped_idx = right_child_idx

        return returned_data

    def move_down(self, popped_idx):
        left_child_idx = 2 * popped_idx
        right_child_idx = 2 * popped_idx + 1

        if left_child_idx >= len(self.heap_array):
            return False
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_idx] < self.heap_array[popped_idx]:
                    return True
                else:
                    return False


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)



# 백트래킹 N queen 알고리즘

def solve_n_queen(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result

def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

a = solve_n_queen(4)
print(a)



# 링크드리스트 연습

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class NodeCon:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
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
        if data == self.head.data:
            self.head = self.head.next
        else:
            node = self.head
            while node.next.data != data:
                node = node.next
            node.next = node.next.next

    def search(self, data):
        node = self.head

        while node:
            if node.data == data:
                return True
            else:
                node = node.next

        return False

    
list = NodeCon(1)

for i in range(2, 11):
    list.insert(i)

list.display()

list.delete(1)
list.delete(6)
list.delete(9)

list.display()

a = list.search(2)
b = list.search(4)
c = list.search(100)

print(a, b, c)




# 더블 링크드리스트 연습

class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None

class NodeCon:
    def __init__(self, data):
        self.head = Node(data)
        self.tail = self.head

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)
            self.tail = self.head
        else:
            node = self.head
            while node.next:
                node = node.next

            new = Node(data)
            node.next = new
            new.prev = node
            self.tail = new

    def display(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if data == self.head.data:
            self.head = self.head.next
            self.head.prev = None
        elif data == self.tail.data:
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            node = self.head
            while data != node.data:
                node = node.next
            node.prev.next = node.next
            node.next.prev = node.prev

    def insert_before(self, data, before):
        if before == self.head.data:
            new = Node(data)
            new.next = self.head
            self.head.prev = new
            self.head = new
        else:
            node = self.head
            while before != node.data:
                node = node.next
            new = Node(data)
            node.prev.next = new
            new.prev = node.prev
            new.next = node
            node.prev = new

    def insert_after(self, data, after):
        if after == self.tail.data:
            new = Node(data)
            self.tail.next = new
            new.prev = self.tail
            self.tail = new
        else:
            node = self.head
            while after != node.data:
                node = node.next
            new = Node(data)
            node.next.prev = new
            new.next = node.next
            new.prev = node
            node.next = new


list = NodeCon(1)

for i in range(2, 11):
    list.insert(i)

list.display()

# delete_list = [1, 3, 6, 9, 10]

# for i in delete_list:
#     list.delete(i)

# list.display()

list.insert_before(0.5, 1)
list.insert_before(9.5, 10)
list.insert_after(8.5, 8)
list.insert_after(2.5, 2)

list.display()
    


# 해쉬테이블 연습 (체이닝)

hash_table = [0 for _ in range(5)]

def get_key(data):
    key = hash(data)
    return key

def hash_function(key):
    address = key % 5
    return address

def store(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        hash_table[address] = [[key, value]]
    else:
        for index in range(len(hash_table[address])):
            if hash_table[address][index][0] == key:
                hash_table[address][index][1] = value
                return
        hash_table[address].append([key, value])

def read(data):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        return None
    else:
        for index in range(len(hash_table[address])):
            if hash_table[address][index][0] == key:
                return hash_table[address][index][1]
        return None

store("Kim", "Korea")
store("Johnson", "USA")
store("Yamamoto", "Japen")
store("Ivanovichi", "Slovania")
print(hash_table)

a = read("Kim")
b = read("Johnson")
c = read("Yamamoto")
d = read("Ivanovichi")
e = read("Xi")
print(a, b, c, d, e)



# 해쉬테이블 연습 (linear probing)

hash_table = [0 for _ in range(5)]

def get_key(data):
    key = hash(data)
    return key

def hash_function(key):
    address = key % 5
    return address

def store(data, value):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        hash_table[address] = [key, value]
    else:
        for index in range(address+1, len(hash_table)):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return
        for index in range(0, address):
            if hash_table[index] == 0:
                hash_table[index] = [key, value]
                return
            elif hash_table[index][0] == key:
                hash_table[index][1] = value
                return

def read(data):
    key = get_key(data)
    address = hash_function(key)

    if hash_table[address] == 0:
        return "No data"
    elif hash_table[address][0] == key:
        return hash_table[address][1]
    else:
        for index in range(address+1, len(hash_table)):
            if hash_table[index] == 0:
                continue
            elif hash_table[index][0] == key:
                return hash_table[index][1]
        for index in range(0, address):
            if hash_table[index] == 0:
                continue
            elif hash_table[index][0] == key:
                return hash_table[index][1]
        return "No data"

store("Kim", "Korea")
store("Johnson", "USA")
store("Yamamoto", "Japen")
store("Ivanovichi", "Slovania")
print(hash_table)

a = read("Kim")
b = read("Johnson")
c = read("Yamamoto")
d = read("Ivanovichi")
e = read("Xi")
print(a, b, c, d, e)



# 버블정렬

def bubble_sort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(0, len(data)-index-1):
            if data[index2] > data[index2+1]:
                data[index2], data[index2+1] = data[index2+1], data[index2]
                swap = True
        if swap == False:
            break
    return data

data = [1, 3, 2, 5, 4]
a = bubble_sort(data)
print(a)

# 삽입정렬

def insertion_sort(data):
    for index in range(len(data)-1):
        for index2 in range(index+1, 0, -1):
            if data[index2] < data[index2-1]:
                data[index2], data[index2-1] = data[index2-1], data[index2]
            else:
                break
    return data

data = [1, 3, 2, 5, 4]
a = insertion_sort(data)
print(a)



# 선택정렬

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand, len(data)):
            if data[lowest] > data[index]:
                lowest = index
        data[lowest], data[stand] = data[stand], data[lowest]
    return data

import random

data_list = random.sample(range(100), 10)
print(data_list)
a = selection_sort(data_list)
print(a)



# 머지 소트

def merge_sort(data):
    if len(data) <= 1:
        return data

    medium = len(data) // 2

    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])

    return merge(left, right)

def merge(left, right):
    left_point = 0
    right_point = 0
    merged = []

    while left_point < len(left) and right_point < len(right):
        if left[left_point] < right[right_point]:
            merged.append(left[left_point])
            left_point += 1
        else:
            merged.append(right[right_point])
            right_point += 1

    while left_point < len(left):
        merged.append(left[left_point])
        left_point += 1

    while right_point < len(right):
        merged.append(right[right_point])
        right_point += 1

    return merged

import random

data_list = random.sample(range(100), 10)
print(data_list)
a = merge_sort(data_list)
print(a)
            


# 퀵소트

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]

    left = [i for i in data[1:] if i < pivot]
    right = [i for i in data[1:] if i > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

import random

data_list = random.sample(range(100), 10)
print(data_list)
a = quick_sort(data_list)
print(a)

# 재귀용법 factorial

def factorial(num):
    if num <= 1:
        return num
    
    return num * factorial(num - 1)

a = factorial(5)
print(a)

# 재귀용법 리스트의 합

def list_sum(data):
    if len(data) <= 1:
        return data[0]
    else:
        return data[0] + list_sum(data[1:])

data_list = [item for item in range(1, 101)]
print(data_list)
a = list_sum(data_list) 
print(a)

# 재귀함수 회문

def palindrome(string):
    if len(string) <= 1:
        return True
    else:
        if string[0] == string[-1]:
            return palindrome(string[1:-1])
        else:
            return False

a = palindrome("Model")
b = palindrome("level")

print(a, b)


# 동적계획법: 피보나치 수열

def fibo(num):
    cache = [0 for index in range(num + 1)]

    cache[0] = 0
    cache[1] = 1

    for index in range(2, num + 1):
        cache[index] = cache[index - 1] + cache[index - 2]

    return cache[num]

for index in range(2, 10):
    a = fibo(index)
    print(a)



# 이진탐색트리

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class NodeCon:
    def __init__(self, data):
        self.head = Node(data)

    def insert(self, data):
        if self.head == None:
            self.head = Node(data)

        else:
            node = self.head
            while True:
                if data < node.data:
                    if node.left == None:
                        node.left = Node(data)
                        break
                    else:
                        node = node.left
                else:
                    if node.right == None:
                        node.right = Node(data)
                        break
                    else:
                        node = node.right

    def search(self, data):
        if self.head == None:
            return "No data in the Tree"

        else:
            node = self.head
            while node:
                if data == node.data:
                    return True
                elif data < node.data:
                    node = node.left
                else:
                    node = node.right
            return False

    def delete(self, data):
        searched = False

        node = self.head
        parent_node = self.head
        while node:
            if data == node.data:
                searched = True
                break
            elif data < node.data:
                parent_node = node
                node = node.left
            else:
                parent_node = node
                node = node.right

        if searched == False:
            print("Delete Failed")
            return False


        if node.left == None and node.right == None:
            if node.data < parent_node.data:
                parent_node.left = None
            else:
                parent_node.right = None
        elif node.left != None and node.right == None:
            if node.data < parent_node.data:
                parent_node.left = node.left
            else:
                parent_node.right = node.left
        elif node.left == None and node.right != None:
            if node.data < parent_node.data:
                parent_node.left = node.right
            else:
                parent_node.right = node.right
        else:
            change_node = node.right
            change_node_parent = node.right

            while change_node.left:
                change_node_parent = change_node
                change_node = change_node.left

            if node.data < parent_node.data:
                change_node_parent.left = change_node.right
                parent_node.left = change_node
                change_node.left = node.left
                change_node.right = node.right
            else:
                change_node_parent.left = change_node.right
                parent_node.right = change_node
                change_node.left = node.left
                change_node.right = node.right
        
        print("Deleted")


import random

test_nums = set()
while len(test_nums) != 100:
    test_nums.add(random.randint(0, 999))

print(test_nums)

test_tree = NodeCon(500)

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



# 순차탐색 연습

def sequential_search(data_list, search_data):
    for index in range(len(data_list)):
        if data_list[index] == search_data:
            return index
    return -1

import random

data_list = []
for _ in range(5):
    data_list.append(random.randint(1, 10))  

print(data_list)
a = sequential_search(data_list, 5)
print(a)



# 이진탐색 연습

def binary_search(data_list, data):
    if len(data_list) == 0:
        return False
    if len(data_list) == 1:
        if data_list[0] == data:
            return True
        else:
            return False

    medium = len(data_list) // 2

    if data_list[medium] == data:
        return True
    else:
        if data_list[medium] > data:
            return binary_search(data_list[:medium], data)
        else:
            return binary_search(data_list[medium+1:], data)

import random

data_list = set()
while len(data_list) !=5:
    data_list.add(random.randint(1, 10))  

data_list = list(data_list)
data_list.sort()
print(data_list)
a = binary_search(data_list, 5)
print(a)


# 너비우선탐색 연습

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start):
    visited = []
    need_visit = []

    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

a = bfs(graph, "A")
print(a)



# 깊이우선 탐색 연습

graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph, start):
    visited = []
    need_visit = []

    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

a = dfs(graph, "A")
print(a)


# 탐욕 알고리즘 동전문제

coin_list = [1, 100, 50, 500]

def min_coin_count(coin_list, value):
    total_coin_count = 0    
    details = []
    coin_list.sort(reverse=True)

    for coin in coin_list:
        coin_count = value // coin
        total_coin_count += coin_count
        value -= coin * coin_count
        details.append((coin, coin_count))

    return total_coin_count, details

a = min_coin_count(coin_list, 4720)
print(a)


# 탐욕알고리즘 부분배낭문제

data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = list()

    for data in data_list:
        if capacity >= data[0]:
            total_value += data[1]
            capacity -= data[0]
            details.append((data[0], data[1], 1))
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append((data[0], data[1], fraction))
            break
    return total_value, details

a = get_max_value(data_list, 30)
print(a)



# 탐욕알고리즘 부분배낭문제

data_list = [(10, 10), (15, 12), (20, 10), (25, 8), (30, 5)]

def get_max_value(data_list, capacity):
    data_list = sorted(data_list, key=lambda x: x[1] / x[0], reverse=True)
    total_value = 0
    details = []

    for data in data_list:
        if capacity > data[0]:
            total_value += data[1]
            capacity -= data[0]
            details.append((data[0], data[1], 1))
        else:
            fraction = capacity / data[0]
            total_value += data[1] * fraction
            details.append((data[0], data[1], fraction))
            break
    return total_value, details

a = get_max_value(data_list, 30)
print(a)


# 다익스트라 알고리즘

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = list()
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if distances[current_node] < current_distance:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, [distance, adjacent])

    return distances

a = dijkstra(mygraph, "A")
print(a)


# 다익스트라 알고리즘

mygraph = {
    'A': {'B': 8, 'C': 1, 'D': 2},
    'B': {},
    'C': {'B': 5, 'D': 2},
    'D': {'E': 3, 'F': 5},
    'E': {'F': 1},
    'F': {'A': 5}
}

import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    queue = []
    heapq.heappush(queue, (distances[start], start))

    while queue:
        current_distance, current_node = heapq.heappop(queue)
        
        if current_distance > distances[current_node]:
            continue

        for adjacent, weight in graph[current_node].items():
            distance = current_distance + weight
            if distance < distances[adjacent]:
                distances[adjacent] = distance
                heapq.heappush(queue, (distance, adjacent))

    return distances

a = dijkstra(mygraph, "A")
print(a)



# 최소힙 연습

class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def insert(self, data):
        if len(self.heap_array) == 1:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True


        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = self.heap_array[parent_idx], self.heap_array[inserted_idx]
            inserted_idx = parent_idx

        return True

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False

        parent_idx = inserted_idx // 2

        if self.heap_array[parent_idx] > self.heap_array[inserted_idx]:
            return True
        else:
            return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return None

        returned_data = self.heap_array[1]
        self.heap_array[1], self.heap_array[-1] = self.heap_array[-1], self.heap_array[1]
        del self.heap_array[-1]

        popped_idx = 1
        left_child_idx = 2 * popped_idx
        right_child_idx = 2 * popped_idx + 1

        while self.move_down(popped_idx):
            if right_child_idx >= len(self.heap_array):
                if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                    self.heap_array[left_child_idx], self.heap_array[popped_idx] =  self.heap_array[popped_idx], self.heap_array[left_child_idx]
                    popped_idx = left_child_idx
            else:
                if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                    if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                        self.heap_array[left_child_idx], self.heap_array[popped_idx] =  self.heap_array[popped_idx], self.heap_array[left_child_idx]
                        popped_idx = left_child_idx
                else:
                    if self.heap_array[right_child_idx] < self.heap_array[popped_idx]:
                        self.heap_array[right_child_idx], self.heap_array[popped_idx] =  self.heap_array[popped_idx], self.heap_array[right_child_idx]
                        popped_idx = right_child_idx
        
        return returned_data

    def move_down(self, popped_idx):
        left_child_idx = 2 * popped_idx
        right_child_idx = 2 * popped_idx + 1

        if left_child_idx >= len(self.heap_array):
            return False
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                return True
            else:
                return False
        else:
            if self.heap_array[left_child_idx] < self.heap_array[right_child_idx]:
                if self.heap_array[left_child_idx] < self.heap_array[popped_idx]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[right_child_idx] < self.heap_array[popped_idx]:
                    return True
                else:
                    return False


heap = Heap(15)
heap.insert(10)
heap.insert(8)
heap.insert(5)
heap.insert(4)
heap.insert(20)
print(heap.heap_array)

print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)
print(heap.pop())
print(heap.heap_array)

# 백트래킹 n queen 문제

def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result

def DFS(N, current_row, current_candidate, final_result):
    if current_row == N:
        final_result.append(current_candidate[:])
        return

    for candidate_col in range(N):
        if is_available(current_candidate, candidate_col):
            current_candidate.append(candidate_col)
            DFS(N, current_row + 1, current_candidate, final_result)
            current_candidate.pop()

def is_available(candidate, current_col):
    current_row = len(candidate)
    for queen_row in range(current_row):
        if candidate[queen_row] == current_col or abs(candidate[queen_row] - current_col) == current_row - queen_row:
            return False
    return True

print(solve_n_queens(5))


# 백트래킹 n queen 연습

def solve_n_queens(N):
    final_result = list()
    DFS(N, 0, [], final_result)
    return final_result

def DFS(N, current_row, candidate, final_result):
    if current_row == N:
        final_result.append(candidate[:])
        return

    for candidate_col in range(N):
        if is_available(candidate, candidate_col):
            candidate.append(candidate_col)
            DFS(N, current_row + 1, candidate, final_result)
            candidate.pop()

def is_available(candidate, candidate_col):
    current_row = len(candidate)

    for queen_row in range(current_row):
        if candidate[queen_row] == candidate_col or abs(candidate[queen_row] - candidate_col) == current_row - queen_row:
            return False
    return True

print(solve_n_queens(4))

# 백트래킹 n queen 연습

def solve_n_queens(N):
    final_result = []
    DFS(N, 0, [], final_result)
    return final_result

def DFS(N, current_row, candidate, final_result):
    if current_row == N:
        final_result.append(candidate[:])
        return

    for current_col in range(N):
        if is_available(current_col, candidate):
            candidate.append(current_col)
            DFS(N, current_row + 1, candidate, final_result)
            candidate.pop()

def is_available(current_col, candidate):
    current_row = len(candidate)
    for queen_row in range(len(candidate)):
        if candidate[queen_row] == current_col or abs(current_col - candidate[queen_row]) == current_row - queen_row:
            return False
    return True

a = solve_n_queens(4)
print(a)

# 버블정렬 연습

def bubble_sort(data):
    for index in range(len(data) - 1):
        swap = False
        for index2 in range(len(data) - index - 1):
            if data[index2] > data[index2 + 1]:
                data[index2], data[index2 + 1] = data[index2 + 1], data[index2]
                swap = True
        if swap == False:
            break
    return data

import random

Testlist = random.sample(range(10), 5)
print(Testlist)

a = bubble_sort(Testlist)
print(a)



# 삽입정렬 연습

def insertion_sort(data):
    for index in range(len(data) - 1):
        for index2 in range(index + 1, 0, -1):
            if data[index2] < data[index2 - 1]:
                data[index2], data[index2 - 1] = data[index2 - 1], data[index2]
            else:
                break
    return data

import random

Testlist = random.sample(range(10), 5)
print(Testlist)

a = insertion_sort(Testlist)
print(a)

# 선택정렬 연습

def selection_sort(data):
    for stand in range(len(data) - 1):
        lowest = stand
        for index in range(stand + 1, len(data)):
            if data[index] < data[lowest]:
                lowest = index
        data[stand], data[lowest] = data[lowest], data[stand]
    return data

import random

Testlist = random.sample(range(20), 10)
print(Testlist)

a = selection_sort(Testlist)
print(a)

# 머지소트 연습

def merge_sort(data):
    if len(data) <= 1:
        return data

    medium = len(data) // 2
    left = merge_sort(data[:medium])
    right = merge_sort(data[medium:])

    return merge(left, right)

def merge(left, right):
    left_point = 0
    right_point = 0
    merged = list()

    while True:
        if left_point < len(left) and right_point < len(right):
            if left[left_point] < right[right_point]:
                merged.append(left[left_point])
                left_point += 1
            else:
                merged.append(right[right_point])
                right_point += 1
        elif left_point < len(left):
            merged.append(left[left_point])
            left_point += 1
        elif right_point < len(right):
            merged.append(right[right_point])
            right_point += 1
        else:
            break
    
    return merged

import random

Testlist = random.sample(range(20), 10)
print(Testlist)

a = merge_sort(Testlist)
print(a)


# 퀵소트 연습

def quick_sort(data):
    if len(data) <= 1:
        return data

    pivot = data[0]
    left = [item for item in data[1:] if item < pivot]
    right = [item for item in data[1:] if item > pivot]

    return quick_sort(left) + [pivot] + quick_sort(right)

import random

Testlist = random.sample(range(20), 10)
print(Testlist)

a = quick_sort(Testlist)
print(a)



# 크루스칼 알고리즘 연습

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}


parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    root1 = parent[node1]
    root2 = parent[node2]

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()

    for node in graph["vertices"]:
        make_set(node)

    edges = graph["edges"]
    edges.sort()

    for edge in edges:
        weight, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(edge)

    return mst

a = kruskal(mygraph)
print(a)



# 프림알고리즘 연습

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)
    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]

    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))
            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)

    return mst

a = prim('A', myedges)
print(a)



# 개선된 프림 알고리즘 연습

mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}    
}

from heapdict import heapdict

def prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0
    for node in graph.keys():
        keys[node] = float('inf')
        pi[node] = None
    keys[start], pi[start] = 0, start

    while keys:
        current_node, curruent_key = keys.popitem()
        mst.append([pi[current_node], current_node, curruent_key])
        total_weight += curruent_key

        for adjacent, weight in mygraph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node

    return mst, total_weight

mst, total_weight = prim(mygraph, 'A')
print(mst)
print(total_weight)


# 크루스칼 알고리즘

mygraph = {
    'vertices': ['A', 'B', 'C', 'D', 'E', 'F', 'G'],
    'edges': [
        (7, 'A', 'B'),
        (5, 'A', 'D'),
        (7, 'B', 'A'),
        (8, 'B', 'C'),
        (9, 'B', 'D'),
        (7, 'B', 'E'),
        (8, 'C', 'B'),
        (5, 'C', 'E'),
        (5, 'D', 'A'),
        (9, 'D', 'B'),
        (7, 'D', 'E'),
        (6, 'D', 'F'),
        (7, 'E', 'B'),
        (5, 'E', 'C'),
        (7, 'E', 'D'),
        (8, 'E', 'F'),
        (9, 'E', 'G'),
        (6, 'F', 'D'),
        (8, 'F', 'E'),
        (11, 'F', 'G'),
        (9, 'G', 'E'),
        (11, 'G', 'F')
    ]
}

parent = dict()
rank = dict()

def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]

def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)

    if rank[root1] > rank[root2]:
        parent[root2] = root1
    else:
        parent[root1] = root2
        if rank[root1] == rank[root2]:
            rank[root2] += 1

def make_set(node):
    parent[node] = node
    rank[node] = 0

def kruskal(graph):
    mst = list()

    for node in graph['vertices']:
        make_set(node)

    edges = graph["edges"]
    edges.sort()

    for edge in edges:
        weight, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            mst.append(edge)

    return mst

a = kruskal(mygraph)
print(a)



# 프림알고리즘

myedges = [
    (7, 'A', 'B'), (5, 'A', 'D'),
    (8, 'B', 'C'), (9, 'B', 'D'), (7, 'B', 'E'),
    (5, 'C', 'E'),
    (7, 'D', 'E'), (6, 'D', 'F'),
    (8, 'E', 'F'), (9, 'E', 'G'),
    (11, 'F', 'G')
]

from collections import defaultdict
from heapq import *

def prim(start_node, edges):
    mst = list()
    adjacent_edges = defaultdict(list)

    for weight, n1, n2 in edges:
        adjacent_edges[n1].append((weight, n1, n2))
        adjacent_edges[n2].append((weight, n2, n1))

    connected_nodes = set(start_node)
    candidate_edge_list = adjacent_edges[start_node]
    heapify(candidate_edge_list)

    while candidate_edge_list:
        weight, n1, n2 = heappop(candidate_edge_list)
        if n2 not in connected_nodes:
            connected_nodes.add(n2)
            mst.append((weight, n1, n2))

            for edge in adjacent_edges[n2]:
                if edge[2] not in connected_nodes:
                    heappush(candidate_edge_list, edge)
    
    return mst

a = prim('A', myedges)
print(a)

# 개선된 프림알고리즘

mygraph = {
    'A': {'B': 7, 'D': 5},
    'B': {'A': 7, 'D': 9, 'C': 8, 'E': 7},
    'C': {'B': 8, 'E': 5},
    'D': {'A': 5, 'B': 9, 'E': 7, 'F': 6},
    'E': {'B': 7, 'C': 5, 'D': 7, 'F': 8, 'G': 9},
    'F': {'D': 6, 'E': 8, 'G': 11},
    'G': {'E': 9, 'F': 11}    
}


from heapdict import heapdict

def prim(graph, start):
    mst, keys, pi, total_weight = list(), heapdict(), dict(), 0

    for node in graph:
        keys[node] = float('inf')
        pi[node] = None

    keys[start], pi[start] = 0, start

    while keys:
        current_node, current_key = keys.popitem()
        mst.append([pi[current_node], current_node, current_key])
        total_weight += current_key

        for adjacent, weight in graph[current_node].items():
            if adjacent in keys and weight < keys[adjacent]:
                keys[adjacent] = weight
                pi[adjacent] = current_node

    return mst, total_weight

mst, total_weight = prim(mygraph, 'A')
print ('MST:', mst)
print ('Total Weight:', total_weight)

# 순차탐색

def sequential_search(data, search_data):
    for index in range(len(data)):
        if data[index] == search_data:
            return index
    return -1

import random

Testlist = random.sample(range(20), 10)
print(Testlist)

a = sequential_search(Testlist, 1)
print(a)

# 이진탐색

def binary_search(data, search_data):
    if len(data) == 1:
        if data[0] == search_data:
            return True
        else:
            return False
    if len(data) == 0:
        return False

    medium = len(data) // 2

    if data[medium] == search_data:
        return True
    elif data[medium] > search_data:
        return binary_search(data[:medium], search_data)
    else:
        return binary_search(data[medium+1:], search_data)

import random

Testlist = random.sample(range(20), 10)
print(Testlist)
Testlist.sort()
print(Testlist)

a = binary_search(Testlist, 1)
print(a)

# 너비우선탐색
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def bfs(graph, start):
    visited = []
    need_visit = []

    need_visit.append(start)

    while need_visit:
        node = need_visit.pop(0)
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

a = bfs(graph, 'A')
print(a)

# 깊이우선탐색
graph = dict()

graph['A'] = ['B', 'C']
graph['B'] = ['A', 'D']
graph['C'] = ['A', 'G', 'H', 'I']
graph['D'] = ['B', 'E', 'F']
graph['E'] = ['D']
graph['F'] = ['D']
graph['G'] = ['C']
graph['H'] = ['C']
graph['I'] = ['C', 'J']
graph['J'] = ['I']

def dfs(graph, start):
    visited = list()
    need_visit = list()

    need_visit.append(start)

    while need_visit:
        node = need_visit.pop()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])

    return visited

a = dfs(graph, 'A')
print(a)
"""
# 탐욕알고리즘 동전문제
coin_list = [1, 100, 50, 500]

def min_coin_count(coin_list, value):
    coin_list.sort(reverse=True)
    total_coin_count = 0
    details = []

    for coin in coin_list:
        coin_count = value // coin
        total_coin_count += coin_count
        value -= coin * coin_count
        details.append((coin, coin_count))

    return total_coin_count, details

a = min_coin_count(coin_list, 4720)
print(a)
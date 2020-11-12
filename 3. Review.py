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

"""

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




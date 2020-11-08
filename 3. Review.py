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

"""

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


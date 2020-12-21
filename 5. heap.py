class Heap:
    def __init__(self, data):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, insert_index):
        if insert_index <= 1:
            return False

        parent_index = insert_index // 2

        if self.heap_array[insert_index] > self.heap_array[parent_index]:
            return True
        else:
            return False

    def insert(self, data):
        # 현재 힙에 아무 것도 없는 경우
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True
        # 일단 데이터를 맨 뒤에 놓고 값에 맞추어 점점 올라가게
        else:
            self.heap_array.append(data)

        insert_index = len(self.heap_array) - 1

        while self.move_up(insert_index):
            parent_index = insert_index // 2
            self.heap_array[insert_index], self.heap_array[parent_index] = self.heap_array[parent_index], self.heap_array[insert_index]
            insert_index = parent_index

        print("Data inserted")
        return

    def move_down(self, popped_index):
        left_child_index = popped_index * 2
        right_child_index = popped_index * 2 + 1

        # child가 아무도 없는 경우
        if left_child_index > len(self.heap_array) - 1:
            return False

        # left child만 있는 경우 
        elif right_child_index > len(self.heap_array) - 1:
            if self.heap_array[popped_index] < self.heap_array[left_child_index]:
                return True
            else:
                return False

        # 두 child 모두 있는 경우
        else:
            if self.heap_array[left_child_index] > self.heap_array[right_child_index]:
                if self.heap_array[popped_index] < self.heap_array[left_child_index]:
                    return True
                else:
                    return False
            else:
                if self.heap_array[popped_index] < self.heap_array[right_child_index]:
                    return True
                else:
                    return False

    def pop(self):
        if len(self.heap_array) <= 1:
            return False

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_index = 1

        while self.move_down(popped_index):
            left_child_index = popped_index * 2
            right_child_index = popped_index * 2 + 1

            # 왼쪽 node만 있을 때
            if right_child_index > len(self.heap_array) - 1:
                if self.heap_array[popped_index] < self.heap_array[left_child_index]:
                    self.heap_array[popped_index], self.heap_array[left_child_index] = self.heap_array[left_child_index], self.heap_array[popped_index]
                    popped_index = left_child_index
            
            # 오른쪽 node도 있을 때
            else:
                if self.heap_array[left_child_index] > self.heap_array[right_child_index]:
                    if self.heap_array[popped_index] < self.heap_array[left_child_index]:
                        self.heap_array[popped_index], self.heap_array[left_child_index] = self.heap_array[left_child_index], self.heap_array[popped_index]
                        popped_index = left_child_index
                                        
                else:
                    if self.heap_array[popped_index] < self.heap_array[right_child_index]:
                        self.heap_array[popped_index], self.heap_array[right_child_index] = self.heap_array[right_child_index], self.heap_array[popped_index]
                        popped_index = right_child_index
        
        print(str(returned_data) + " POPPED!")            
        return returned_data



heap = Heap(30)
heap.insert(19)
heap.insert(21)
heap.insert(1)
heap.insert(49)
heap.insert(200)
heap.insert(100)

print(heap.heap_array)

heap.pop()

print(heap.heap_array)

heap.pop()

print(heap.heap_array)
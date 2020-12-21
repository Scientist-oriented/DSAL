'''
# 트리순회문제

import sys
sys.stdin=open("input.txt", "rt")

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def pre_order(node):
    print(node.data, end='')
    if node.left != '.':
        pre_order(tree[node.left])
    if node.right != '.':
        pre_order(tree[node.right])

def in_order(node):
    if node.left != '.':
        in_order(tree[node.left])
    print(node.data, end='')
    if node.right != '.':
        in_order(tree[node.right])

def post_order(node):
    if node.left != '.':
        post_order(tree[node.left])
    if node.right != '.':
        post_order(tree[node.right])
    print(node.data, end='')

n = int(input())
tree = dict()
for i in range(n):
    data, left, right = input().split()
    tree[data] = Node(data, left, right)

pre_order(tree['A'])
print()
in_order(tree['A'])
print()
post_order(tree['A'])
'''
# 트리의 높이와 너비 문제

import sys
sys.stdin=open("input.txt", "rt")

class Node:
    def __init__(self, number, left_node, right_node):
        self.parent = -1
        # 높이를 알아야하니까 parent를 저장
        self.number = number
        self.left_node = left_node
        self.right_node = right_node


def in_order(node, level):
    # 중위순회
        # 각 Node의 x좌표값과 level를 알 수 있음.
        # 이것을 다 저장해놓고 나중에 후처리를 하기 보다는
        # 여기서 답이 원하는 것을 바로 구하는 함수를 작성한다.
    global level_depth, x
    # x 값은 현재 순회의 대상인 Node의 x좌표를 의미 ("좌 -> 우"일때 1씩 증가)
    level_depth = max(level_depth, level)
    if node.left_node != -1:
        in_order(tree[node.left_node], level + 1)
        # 재귀함수부분: 자식 node로 내려가면 level을 하나 더한다.

    level_min[level] = min(level_min[level], x)
        # 그 레벨에서 가장 작은 x좌표를 저장
    level_max[level] = max(level_max[level], x)
        # 그 레벨에서 가장 큰 x좌표를 저장
        # 최종적으로 너비를 구하는 것이므로 number를 저장하는게 아니라 x좌표를 저장해야함.
    x += 1
        # 순회하면서 level의 최대값, 최소값을 저장하고
        # x좌표는 하나 늘린다.
   
    if node.right_node != -1:
        in_order(tree[node.right_node], level + 1)

n = int(input())
tree = {}
    # number별로 Node객체를 저장해놓는 장소
    # Node에 개별적으로 접근해야할 때 유용함.
level_min = [n]
    # 각 레벨의 최대 x좌표값
level_max = [0]
    # 각 레벨의 최대 x좌표값
root = -1
x = 1
level_depth = 1
    # 레벨이 총 몇개 있는지 확인함

for i in range(1, n + 1):
    tree[i] = Node(i, -1, -1)
    # 그냥 class만 선언하면 개별 Node에 접근하기 어려우니까 dict로 저장해놓음.
    level_min.append(n)
    level_max.append(0)
    # tree가 일자로 쭉 이어지면 최대 level이 n까지 발생하므로 미리 최대값으로 만들어 놓는다.
    # 물론 트리 가지가 많이 뻗어나가면 다 안쓸 수도 있음

for _ in range(n):
    number, left_node, right_node = map(int, input().split())
    tree[number].left_node = left_node
    tree[number].right_node = right_node
    # 부모값을 저장하는 방법: 이미 Node가 선언되어 있어야 가능
    # 따라서 위에서 미리 Node 선언함
    if left_node != -1:
        tree[left_node].parent = number
    if right_node != -1:
        tree[right_node].parent = number

for i in range(1, n + 1):
    if tree[i].parent == -1:
        root = i
    # 순차탐색을 통해 Node를 찾음

in_order(tree[root], 1)

result_level = 1
result_width = level_max[1] - level_min[1] + 1
    # 최댓값을 찾아야하므로 최소값인 level 1에서 부터 시작

for i in range(2, level_depth + 1):
    width = level_max[i] - level_min[i] + 1
    # 각 level의 width 값을 구해서
    if result_width < width:
        result_level = i
        result_width = width
        # 지금까지의 최댓값이면 변수에 저장한다.

print(result_level, result_width)


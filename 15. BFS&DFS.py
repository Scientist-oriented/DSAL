# 그래프 구현

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

print(graph)

# 너비우선탐색 구현

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

# 깊이우선탐색 구현

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
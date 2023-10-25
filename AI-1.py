from collections import deque

def add_edge(graph, u, v):
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]

    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

def recursive_dfs(graph, start, visited=None):
    if visited is None:
        visited = set()

    if start not in visited:
        print(start, end=' ')
        visited.add(start)

        for neighbor in graph[start]:
            recursive_dfs(graph, neighbor, visited)

def recursive_bfs(graph, start, queue, visited):
    if not queue:
        return

    current = queue.popleft()
    print(current, end=' ')

    for neighbor in graph[current]:
        if neighbor not in visited:
            queue.append(neighbor)
            visited.add(neighbor)

    recursive_bfs(graph, start, queue, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("\nBFS:")
    recursive_bfs(graph, start, queue, visited)

# Take user input to construct the graph
graph = {}
num_edges = int(input("Enter the number of edges: "))

for _ in range(num_edges):
    u, v = map(int, input("Enter edge (u v): ").split())
    add_edge(graph, u, v)

# Take user input for the starting vertex
start_vertex = int(input("Enter the starting vertex: "))

# Perform DFS and BFS
print("\nDFS:")
recursive_dfs(graph, start_vertex)
bfs(graph, start_vertex)

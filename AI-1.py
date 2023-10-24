from collections import deque

def dfs(graph, vertex, visited):
    if vertex not in visited:
        print(vertex, end=' ')  # Process the current vertex
        visited.add(vertex)

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                dfs(graph, neighbor, visited)

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    while queue:
        vertex = queue.popleft()
        print(vertex, end=' ')  # Process the current vertex

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                queue.append(neighbor)
                visited.add(neighbor)

def main():
    graph = {}
    
    # Input graph edges
    num_edges = int(input("Enter the number of edges: "))
    for _ in range(num_edges):
        src, dest = input("Enter edge (source destination): ").split()
        if src not in graph:
            graph[src] = []
        if dest not in graph:
            graph[dest] = []
        graph[src].append(dest)
        graph[dest].append(src)

    # Input starting vertex
    start_vertex = input("Enter the starting vertex: ")

    # Initialize a set to keep track of visited vertices
    visited = set()

    # Perform DFS
    print("\nDFS Traversal:")
    dfs(graph, start_vertex, visited)

    # Reset visited set for BFS
    visited = set()

    # Perform BFS
    print("\nBFS Traversal:")
    bfs(graph, start_vertex)

if __name__ == "__main__":
    main()

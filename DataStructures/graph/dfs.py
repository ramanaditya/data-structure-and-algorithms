def dfs(at, graph, visited):
    if visited[at]:
        return
    visited[at] = True
    print(at, end=" -> ")
    neighbours = graph[at]
    for next in neighbours:
        dfs(next, graph, visited)


if __name__ == "__main__":
    n = int(input("No. of Nodes : "))
    graph = []
    for i in range(n):
        graph.append(list(map(int, input("Nodes linked with {} : ".format(i)).split())))
    start_node = int(input("Starting Node : "))
    # graph = [[1, 2], [3], [1], [2], [3, 5], [5]]
    visited = [False] * n
    print("\nNodes in DFS are : ", end=" ")
    dfs(start_node, graph, visited)
    print(" / ")

"""
Input : 
No. of Nodes : 6
Nodes linked with 0 : 1 2
Nodes linked with 1 : 3
Nodes linked with 2 : 1
Nodes linked with 3 : 2
Nodes linked with 4 : 3 5
Nodes linked with 5 : 5
Starting Node : 4

Output:
Nodes in DFS are :  4 -> 3 -> 2 -> 1 -> 5 ->  / 
"""

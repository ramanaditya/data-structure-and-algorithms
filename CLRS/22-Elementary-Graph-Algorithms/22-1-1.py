"""
22.1-1
Given an adjacency-list representation of a directed graph, how long does it take to compute the out-degree of every
vertex? How long does it take to compute the in-degrees?

eg.,
Given adjacency List

1 -> 2 -> 4 -> /
2 -> 5 -> /
3 -> 6 -> 5 -> /
4 -> 2 -> /
5 -> 4 -> /
6 -> 6 -> /
"""


def outdegree(graph):
    """
    To find the out degree we need to scan through all the vertices and all the edges associated with that vertex so
     the time it takes is O(V+E)
     """
    out = []
    for i in range(len(graph)):
        out.append(len(graph[i]))
    return out


def indegree(graph):
    """
    To find the in degree we need to scan through all the vertices and all the edges associated with that vertex so
     the time it takes is O(V+E), Here we need to take count of all the vertices that appears in the adjacency list
     """
    in_degree = [0] * len(graph)
    for i in graph:
        for j in range(len(i)):
            in_degree[i[j] - 1] += 1
    return in_degree


if __name__ == "__main__":
    graph = [[2, 4], [5], [6, 5], [2], [4], [6]]
    print("Given Adjacency List is :")
    for i in range(len(graph)):
        print("{0} : {1}".format(i + 1, graph[i]))
    out_degree = outdegree(graph)
    in_degree = indegree(graph)
    print("\nOut Degree :", end=" ")
    for j in range(len(out_degree)):
        print("{0} : {1}".format(j + 1, out_degree[j]), end=" , ")
    print("\nIn Degree :", end=" ")
    for j in range(len(in_degree)):
        print("{0} : {1}".format(j + 1, in_degree[j]), end=" , ")
    print("\n")
    print("Out Degree Explanation : ", outdegree.__doc__)
    print("\nIn Degree Explanation : ", indegree.__doc__)

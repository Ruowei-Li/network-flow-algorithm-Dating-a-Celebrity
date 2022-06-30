import sys
import math
import copy

def create_graph(c_list, donor_list):
    N = len(c_list)
    M = len(donor_list)
    capacity = M
    graph = [[0 for i in range(N+M+2)] for j in range(N+M+2)]
    for i in range(1, M + 1):
        graph[0][i] = 1
        a_list = donor_list[i-1]
        for c in a_list:
            graph[i][M + 1 + c] = 1
    return graph

def update_capacity(N, M, graph, capacity):
    for j in range(M + 1, N + M + 1):
        graph[j][N + M + 1] = capacity
    return graph
    
def get_optimal(c_list, donor_list, min_bound, max_bound):
    N = len(c_list)
    M = len(donor_list)
    source = 0
    sink = N + M + 1
    graph = create_graph(c_list, donor_list)
    graph1 = copy.deepcopy(graph)
    while min_bound < max_bound:
        mid = (min_bound + max_bound)//2
        graph1 = copy.deepcopy(graph)
        graph2 = update_capacity(N, M, graph1, mid)
        if network_flow(graph2, source, sink, M):
            max_bound = mid 
        else:
            min_bound = mid + 1
    return max_bound

def BFS(graph, s, t, parent):
    visited = [False] * len(graph)
    queue = []
    queue.append(s)
    visited[s] = True
 
    while queue:
        u = queue.pop(0)
        for ind in range(len(graph[u])):
            if visited[ind] is False and graph[u][ind] > 0:
                queue.append(ind)
                visited[ind] = True
                parent[ind] = u
 
    return True if visited[t] else False
 
 
def network_flow(graph, source, sink, M):
    parent = [-1] * (len(graph))
    max_flow = 0
    while BFS(graph, source, sink, parent):
        path_flow = float("Inf")
        s = sink
        while s != source:
            path_flow = min(path_flow, graph[parent[s]][s])
            s = parent[s]
        max_flow += path_flow
        v = sink
        while v != source:
            u = parent[v]
            graph[u][v] -= path_flow
            graph[v][u] += path_flow
            v = parent[v]
    return max_flow == M

def main(content):
    num_events = int(content[0])
    line_index = 1
    for i in range(num_events):

        num = content[line_index]
        num = num.strip().split()
        N = int(num[0])
        M = int(num[1])
        celebrities_list = []
        donor_list = []
        for c in range((line_index + 1), (line_index + N + 1)):
            celebrities = content[c].strip().split()
            celebrities_list.append(celebrities[0])
        for d in range((line_index + N + 1), (line_index + N + M + 1)):
            c_list = content[d].strip().split()
            if len(c_list) >= 2:
                index_list = []
                for c in c_list[1:]:
                    index = celebrities_list.index(c)
                    index_list.append(index)
                donor_list.append(index_list)
        c_list = [i for i in range(len(celebrities_list))]

        min_bound = math.ceil(len(donor_list)/N)
        max_bound = len(donor_list)
        if min_bound == max_bound:
            print("Event {}: {}".format(i+1, max_bound))
        else:
            max_bound = get_optimal(c_list, donor_list, min_bound, max_bound)
            print("Event {}: {}".format(i+1, max_bound))
        line_index += N + M + 1

content = sys.stdin.readlines()
main(content)

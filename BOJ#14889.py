from itertools import combinations
import sys
N = int(sys.stdin.readline()) 
M = N//2
graph = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]
new_graph = [sum(i) + sum(j) for i, j in zip(graph, zip(*graph))]
sum_graph = sum(new_graph) // 2

mins = 100*((N-1)*N)//2
for l in combinations(new_graph[:-1], M):
    mins = min(mins, abs(sum_graph - sum(l)))
print(mins)
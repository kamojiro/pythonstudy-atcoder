from math import log2
from collections import deque
import sys
input = sys.stdin.readline
def main():
    N = int( input())
    LogN = int( log2(N))+1 # log of edge number
    E = [ list( map( int, input().split()))[1:] for i in range(N)]
    parent = [[-1]*(LogN) for _ in range(N)]
    start = 0
    deq = deque([0])
    depth = [-1]*N
    depth[start] = 0
    while deq: #calculate depth and calculate the parent of each vertex by 2**0 = 1
        v = deq.popleft()
        nextdepth = depth[v] + 1
        for w in E[v]:
            if depth[w] == -1:
                depth[w] = nextdepth
                parent[w][0] = v
                deq.append(w)

    for k in range(LogN-1):
        for v in range(N):
            if (parent[v][k] < 0):
                parent[v][k+1] = -1
            else:
                parent[v][k+1] = parent[ parent[v][k]][k]

    Q = int( input())
    for _ in range(Q):
        u, v = map( int, input().split())
        if depth[u] > depth[v]:
            u, v = v, u
        for k in range(LogN):
            if( (depth[v] - depth[u]) >> k & 1):
                v = parent[v][k]
        if u == v:
            print(u)
            continue
        for k in range(LogN-1, -1, -1):
            if parent[u][k] != parent[v][k]:
                u = parent[u][k]
                v = parent[v][k]
        print(parent[u][0])

if __name__ == '__main__':
    main()

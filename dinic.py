#!/usr/bin/ python3.8
import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

from collections import deque


class Dinic:
    def __init__(self, N, source, sink):
        self.N = N
        self.G = [[] for _ in range(N)]
        self.source = source
        self.sink = sink

    def add_edge(self, fr, to, cap):
        n1 = len(self.G[fr])
        n2 = len(self.G[to])
        self.G[fr].append([to, cap, n2])
        self.G[to].append([fr, 0, n1])  # 逆辺を cap 0 で追加

    def add_edge_undirected(self, fr, to, cap):
        n1 = len(self.G[fr])
        n2 = len(self.G[to])
        self.G[fr].append([to, cap, n2])
        self.G[to].append([fr, cap, n1])

    def bfs(self):
        level = [0] * self.N
        G = self.G; source = self.source; sink = self.sink
        q = deque([source])
        level[source] = 1
        pop = q.popleft; append = q.append
        while q:
            v = pop()
            lv = level[v] + 1
            for to, cap, rev in G[v]:
                if not cap:
                    continue
                if level[to]:
                    continue
                level[to] = lv
                if to == sink:
                    self.level = level
                    return
                append(to)
        self.level = level

    def dfs(self, v, f):
        if v == self.sink:
            return f
        G = self.G
        prog = self.progress
        level = self.level
        lv = level[v]
        E = G[v]
        for i in range(prog[v], len(E)):
            to, cap, rev = E[i]
            prog[v] = i
            if not cap:
                continue
            if level[to] <= lv:
                continue
            x = f if f < cap else cap
            ff = self.dfs(to, x)
            if ff:
                E[i][1] -= ff
                G[to][rev][1] += ff
                return ff
        return 0

    def max_flow(self):
        INF = 10**18
        flow = 0
        while True:
            self.bfs()
            if not self.level[self.sink]:
                return flow
            self.progress = [0] * self.N
            while True:
                f = self.dfs(self.source, INF)
                if not f:
                    break
                flow += f
        return flow


N, M, D = map(int, readline().split())
m = map(int, read().split())
U, V, P, Q, W = zip(*zip(m, m, m, m, m))
X = [(u << 32) + p for u, p in zip(U, P)]
Y = [(v << 32) + q + D for v, q in zip(V, Q)]
nodes = sorted(set(X + Y))
ind = {x: i for i, x in enumerate(nodes)}
L = len(nodes)
source = L
sink = L + 1
dinic = Dinic(len(nodes) + 2, source, sink)
INF = 10 ** 18

add = dinic.add_edge

u, t = divmod(nodes[0], 1 << 32)
if u == 1:
    add(source, 0, INF)
u, t = divmod(nodes[-1], 1 << 32)
if u == N:
    add(L - 1, sink, INF)
for i, (x, y) in enumerate(zip(nodes, nodes[1:])):
    if x >> 32 == y >> 32:
        add(i, i + 1, INF)

for x, y, w in zip(X, Y, W):
    add(ind[x], ind[y], w)

f = dinic.max_flow()
print(f)

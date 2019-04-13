#ノードn個、エッジe本のグラフの入力
n,e = map( int, input().split())
p = []
for i in range(e):
    p.append(list(map(int, input().split())))
    
#隣接リスト
l = [[] for i in range(n)]
for pi in p:  #0-originedに注意
    l[pi[0]].append(pi[1])
    l[pi[1]].append(pi[0])
print(l)

#重み付き隣接リスト
lw = [[] for l in range(n+1)]
for path in p:
    lw[path[0]].append((path[1],path[2]))
    lw[path[1]].append((path[0],path[2]))
print(lw)

#重みなし隣接行列???
m =[ [0]*n for i in range(n)]
for path in p:
    m[path[0]-1][path[1]-1] = 1
print(m) 

#重みあり隣接行列???
mw =[ [0]*n for i in range(n)]
for path in p:
    mw[path[0]-1][path[1]-1] = path[2]
print(mw) 

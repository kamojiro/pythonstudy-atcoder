#classの方が遅いっぽいな
class UnionFind():
    def __init__(self,size):
        self.table = [ i for i in range(size)]
        
    def find(self,x):
        p = self.table[x]
        if p == x:
            return x
        a = self.find(p)
        self.table[x] = a
        return a
 
    def union(self, x, y):
        bx, by = self.find(x), self.find(y)
        self.table[y] = bx
        self.table[by] = bx

N, Q = map( int, input().split())
L = UnionFind(N)
for _ in range(Q):
    p, a, b = map( int, input().split())
    a, b = a-1, b-1
    if p == 0:
        L.union(a,b)
    else:
        if L.find(a) == L.find(b):
            print('Yes')
        else:
            print('No')

#こっちのほうが早い。
#defしないほうが早い。たぶん。
# def find(A,x):
#     p = A[x]
#     if p == x:
#         return x
#     a = find(A,p)
#     A[x] = a
#     return a
 
# def union(A, x, y):
#     bx, by = find(A,x), find(A,y)
#     A[y] = bx
#     A[by] = bx

# N, Q = map( int, input().split())
# L = [ i for i in range(N)]
# for _ in range(Q):
#     p, a, b = map( int, input().split())
#     a, b = a-1, b-1
#     if p == 0:
#         union(L,a,b)
#     else:
#         if find(L,a) == find(L,b):
#             print('Yes')
#         else:
#             print('No')

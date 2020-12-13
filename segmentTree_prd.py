# https://atcoder.jp/contests/abc185/submissions/18753714

import sys
input = sys.stdin.readline
N,Q = map(int,input().split())
A = list(map(int,input().split()))
TXY = [tuple(map(int,input().split())) for i in range(Q)]

def ceil_pow2(n: int) -> int:
    x = 0
    while (1 << x) < n: x += 1
    return x

class segtree:
    def __init__(self, op, e, v: list):
        self._n = len(v)
        self.log = ceil_pow2(self._n)
        self.size = 1 << self.log
        self.op = op; self.e = e
        self.d = [self.e()] * (self.size * 2)
        for i in range(self._n): self.d[self.size + i] = v[i]
        for i in range(self.size - 1, 0, -1): self.__update(i)

    def set_(self, p: int, x: int):
        assert 0 <= p and p < self._n
        p += self.size
        self.d[p] = x
        for i in range(1, self.log + 1): self.__update(p >> i)

    def get(self, p: int):
        assert 0 <= p and p < self._n
        return self.d[p + self.size]

    def prod(self, l: int, r: int):
        assert 0 <= l and l <= r and r <= self._n
        l += self.size; r += self.size
        sml, smr = self.e(), self.e()
        while l < r:
            if l & 1: sml = self.op(sml, self.d[l]); l += 1
            if r & 1: r -= 1; smr = self.op(self.d[r], smr)
            l >>= 1; r >>= 1
        return self.op(sml, smr)

    def __update(self, k: int): self.d[k] = self.op(self.d[k * 2], self.d[k * 2 + 1])

segt = segtree(lambda x,y:x^y, lambda:0, A)
ans = []
for t,x,y in TXY:
    x -= 1
    if t==1:
        v = segt.get(x)
        segt.set_(x,v^y)
    else:
        ans.append(segt.prod(x,y))
print(*ans, sep='\n')

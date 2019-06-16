class SegmentTree:
    def __init__(self, n, cal, unit): #example (12, min, 2**31-1)
        for k in range(40):
            if 2**k > N:
                break
        self.powers = pow(2,k)
        self.segTree = [unit]*(2*self.powers)
        self.cal = cal
        self.unit = unit
    
    def update(self, i, x):#i番目(0-indexed)にx代入, segTree = [0,*,*,...], 1-indexed, N < k
        i += self.powers
        self.segTree[i] = x
        while i > 1:
            i //= 2
            self.segTree[i] = self.cal(self.segTree[i*2],self.segTree[i*2+1])

    def getCal(self, i, j, k=1, l=0, r=-1): #get self.cal of [i,j)!!!!!
        if r < 0: #initization, we want to r = self.powers as an initial value.
            r = self.powers
        if j <= l or r <= i:
            return self.unit
        if i <= l and r <= j:
            return self.segTree[k]
        return self.cal( self.getCal(i ,j, k*2, l, (l+r+1)//2) ,self.getCal(i ,j, k*2+1, (l+r+1)//2, r))

N, Q = map( int, input().split())
segmentTree = SegmentTree(N, min, 2**31-1)
for _ in range(Q):
    com, x, y = map( int, input().split())
    if com == 0:#0-indexed
        segmentTree.update(x,y)
    else:#""[x,y]"
        print(segmentTree.getCal(x,y+1)) #remark. we need "+1".


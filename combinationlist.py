#Qはmod
# Q = ax + b
# a = Q//x
# b = Q%x
# (Q-b)/a * y = 1
# (Q-b)*y = a
# b+y = -a
# y = -a*b^-1
# よって、inv[x] = (-(Q//x)*inv[Q%x])%Q
def getInv(N):
    inv = [0] * (N + 1)
    inv[1] = 1
    for i in range(2, N + 1):
        inv[i] = (-(Q // i) * inv[Q % i]) % Q
    return inv

def getCmb(N):
    inv = getInv(N)
    nCr = [1] * (N + 1)
    for i in range(1, N + 1):
        nCr[i] = (nCr[i - 1] * (N - i + 1) * inv[i]) % Q
    return nCr

from math import factorial

N = int( input())
Q = 10**9 + 7
invs = getInv(N)
for i in range(N):
    print(i*invs[i]%Q)

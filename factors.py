def Primefactors(N):# Nより小さい自然数の素因数の個数と約数の個数を返すO(Nlog(N))
    Ints = [ i for i in range(N)]
    Primefactors = [0]*N
    Factors = [1]*N
    for i in range(2, N):
        if Ints[i] == 1:
            continue
        for j in range(1, N):
            if i*j < N:
                t = 1
                while Ints[i*j]%i == 0:
                    Ints[i*j] //= i
                    Primefactors[i*j] += 1
                    t += 1
                Factors[i*j] *= t
            else:
                break
    return Primefactors, Factors

def factors(N): #約数を全て求める。ただし、順不同
    from collections import deque
    ret = deque()
    middle = int( N**(1/2))
    for i in range(1, middle):
        if N%i == 0:
            ret.append(i)
            ret.append(N//i)
            
    if N%middle == 0:
        ret.append(middle)
        if middle != N//middle:
            ret.append(N//middle)
    return ret
    

N = int( input())
# P, F = Primefactors(N)
# print(P, F)
print(factors(N).pop())
# local でしか import してないはずでは？？？
print([ r for r in factors(N)])
# factors @python
# 15! > 10**12: 241ms
# 2**40 > 10**12: 224ms

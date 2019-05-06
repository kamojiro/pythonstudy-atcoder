# work = [True] * 100001
# work[0] = False
# work[1] = False
# primes = []
# for i in range(100001):
#     if work[i]:
#         for j in range(2* i, 100001, i):
#             work[j] = False

def eratosththenes(N):
    work = [True] * (N+1)
    work[0] = False
    work[1] = False
    for i in range(N+1):
        if work[i]:
            for j in range(2* i, N+1, i):
                work[j] = False
    return work

N = int( input())
Primelist = eratosththenes(N)
Primes = [ p for p in range(N+1) if Primelist[p] == 1]
print(Primes)
    

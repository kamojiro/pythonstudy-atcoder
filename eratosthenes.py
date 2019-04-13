work = [True] * 100001
work[0] = False
work[1] = False
primes = []
for i in range(100001):
    if work[i]:
        for j in range(2* i, 100001, i):
            work[j] = False

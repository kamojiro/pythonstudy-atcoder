def count_prime_factors(N): #素因数
    ret = 0
    middle = int( N**(1/2))
    tmp = N
    for i in range(2, middle+1):
        if tmp%i == 0:
            ret += 1
            while tmp%i == 0:
                tmp //= i
    if tmp != 1:
        ret += 1
    return ret

def prime_factors(N): #素因数 1を含まないことに注意
    ret = []
    middle = int( N**(1/2))
    tmp = N
    for i in range(2, middle+1):
        if tmp%i == 0:
            while tmp%i == 0:
                tmp //= i
            ret.append(i)
    if tmp != 1:
        ret.append(tmp)
    return ret

def main():
    print( prime_factors(6), [2,3])
    print( prime_factors(2), [2])
    print( prime_factors(10**9+7), [10**9+7])
if __name__ == '__main__':
    main()

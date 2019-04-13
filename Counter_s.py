from collections import Counter
*A, = map(int, input().split())
B = Counter(A)
print(B)
print(B[1])
print(B.keys())
print(B.values())
print(B.items())

n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

for i in range(k):
    minA = A.index(min(A)) 
    maxB = B.index(max(B))
    A[minA], B[maxB] = B[maxB], A[minA]

print(sum(A))

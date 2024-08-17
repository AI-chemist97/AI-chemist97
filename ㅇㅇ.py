def back(n,m,a):
    if a==n:
        print(a)
        return
    print(a,""," ")

import sys

n,m=sys.stdin.readline().split()
for j in range(m):
    em = []
    for j in range(1,n+1):
        em.add(j)
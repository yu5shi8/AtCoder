# -*- coding: utf-8 -*-
# C - Traveling Salesman around Lake
# https://atcoder.jp/contests/abc160/tasks/abc160_c

K, N = map(int, input().split())
A = list(map(int, input().split()))
check = [0] * N
check[0] = A[0]+K - A[-1]

for i in range(N-1):
    check[i+1] = abs(A[i+1] - A[i])

ans = sum(check) - max(check)
print(ans)

# 23:28 - 0:08（WA）
# 13:37 - 15:46（AC）

# -*- coding: utf-8 -*-
# C - Tsundoku
# https://atcoder.jp/contests/abc172/tasks/abc172_c

N, M, K = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

check_A = [0]
check_B = [0]

for a in range(N):
    check_A.append(check_A[a] + A[a])

for b in range(M):
    check_B.append(check_B[b] + B[b])

ans = 0
j = M

for i in range(N+1):
    if check_A[i] > K:
        break
    while check_B[j] > K - check_A[i]:
        j -= 1
    ans = max(ans, i+j)

print(ans)

# 21:03 - 22:27（TLE）
# 21:57 - 22:26（TLE）
# 22:31 - 22:36（WA）
# 16:26 - 16:34（AC）

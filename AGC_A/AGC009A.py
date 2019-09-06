# -*- coding: utf-8 -*-
# A - Multiple Array
# https://atcoder.jp/contests/agc009/tasks/agc009_a

N = int(input())
A = []
B = []
ans = 0

for i in range(N):
    a, b = map(int, input().split())
    A.append(a)
    B.append(b)

for i in range(N-1, -1, -1):
    a, b = (A[i] + ans), B[i]
    if a % b != 0:
        ans += b - a % b

print(ans)

# [1] 16:40 - 17:16 / 17:30 - 18:28 / 18:48 -（解説・解答を閲覧）19:50
# [2] 20:35 - 20:45（WA）- 20:53（AC）

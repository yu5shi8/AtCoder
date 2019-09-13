# -*- coding: utf-8 -*-
# A - Zero-Sum Ranges
# https://atcoder.jp/contests/agc023/tasks/agc023_a

N = int(input())
A = list(map(int, input().split()))
S = [0] * (N + 1)
S[0] = A[0]

for i in range(N):
    S[i+1] = S[i] + A[i]
S.sort()

ans = 0
cnt = 1
num = -10 ** 20

for i in range(N+1):
    if num != S[i]:
        ans += cnt * (cnt-1) // 2
        num = S[i]
        cnt = 1
    else:
        cnt += 1

ans += cnt * (cnt-1) // 2

print(ans)

# [1] 17:56 - 18:26（WA）- 18:47（WA）-（解説・解答を閲覧）19:17
# [2] 19:56 - 20:15
# [3] 7:38 - 7:49（AC）

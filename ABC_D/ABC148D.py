# -*- coding: utf-8 -*-
# D - Brick Break
# https://atcoder.jp/contests/abc148/tasks/abc148_d

N = int(input())
a = list(map(int, input().split()))

target = 1
ans = 0

for i in range(N):
    if a[i] == target:
        target += 1
    else:
        ans += 1

if ans == N:
    ans = -1

print(ans)

# 21:14 - 22:09（WA）

# -*- coding: utf-8 -*-
# C - Lower
# https://atcoder.jp/contests/abc139/tasks/abc139_c

N = int(input())
H = list(map(int, input().split())) + [10**9 + 10]
check = 0
ans = [0]

for i in range(1, N + 1):
    if H[i - 1] >= H[i]:
        check += 1
    else:
        if min(ans) < check:
            ans.append(check)
            check = 0

print(max(ans))

# 21:08 - 21:22（TLE）- 21:39（AC）

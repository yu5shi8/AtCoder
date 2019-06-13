# -*- coding: utf-8 -*-
# C - Typical Stairs
# https://atcoder.jp/contests/abc129/tasks/abc129_c

mod = 10**9 + 7
n, m = map(int, input().split())
a = [int(input()) for _ in range(m)]

is_broken = [1] * (n+1)

for i in range(m):
    is_broken[a[i]] = 0

step = [i for i in range(n+1)]
step[0] = 1

for i in range(n):
    if i - 1 >= 0:
        step[i+1] = step[i] * is_broken[i] + step[i-1] * is_broken[i-1]
    else:
        step[i+1] = step[i] * is_broken[i]
    step[i+1] %= mod

print(step[n])

# 22:45 - 23:22
# 16:10 - 16:48（TLE）- 17:00（AC）

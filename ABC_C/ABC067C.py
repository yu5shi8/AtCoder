# -*- coding: utf-8 -*-
# C - Splitting Pile
# https://atcoder.jp/contests/abc067/tasks/arc078_a

N = int(input())
a = list(map(int, input().split()))
ans = 10**10

for i in range(1, N):
    if i == 1:
        x = sum(a[:i])
        y = sum(a[i:])
    else:
        x += a[i-1]
        y -= a[i-1]
    check = abs(x - y)
    if ans > check:
        ans = check

print(ans)

# 11:01 - 11:09（TLE）- 11:19（AC）

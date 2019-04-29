# -*- coding: utf-8 -*-
# B - Shift only
# https://atcoder.jp/contests/abc081/tasks/abc081_b

n = int(input())
a = list(map(int, input().split()))
ans = 1000000000

for i in range(n):
    count = 0
    while a[i] % 2 == 0:
        a[i] = a[i]//2
        count += 1
    if ans >= count:
        ans = count
print(ans)

# 17:37 - 17:45

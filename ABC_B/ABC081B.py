# -*- coding: utf-8 -*-
# ABC081B - Shift only
# https://atcoder.jp/contests/abs/tasks/abc081_b

n = int(input())
l = list(map(int, input().split()))
ans = 10000000000

for i in range(n):
    count = 0
    while l[i] % 2 == 0:
        l[i] = int(l[i] / 2)
        count += 1
    if ans >= count:
        ans = count
print(ans)
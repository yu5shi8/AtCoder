# -*- coding: utf-8 -*-
# B - Cakes and Donuts
# https://atcoder.jp/contests/abc105/tasks/abc105_b

n = int(input())

for a in range(n+1):
    for b in range(n+1):
        ans = 4*a + 7*b
        if ans == n:
            print('Yes')
            exit()
print('No')


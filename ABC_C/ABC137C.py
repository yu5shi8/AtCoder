# -*- coding: utf-8 -*-
# C - Green Bin
# https://atcoder.jp/contests/abc137/tasks/abc137_c

n = int(input())
s = [''.join(sorted(input())) for _ in range(n)]

dct = {}
ans = 0

for i in range(n):
    item = s[i]
    if item in dct:
        dct[item] += 1
    else:
        dct.setdefault(item, 0)
    num = dct[item]
    ans += num

print(ans)

# 21:08 - 21:44（TLE）- 22:14（WA）- 22:25（WA）
# 8:39（WA）
# 

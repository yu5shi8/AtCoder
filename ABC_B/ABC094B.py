# -*- coding: utf-8 -*-
# B - Toll Gates
# https://atcoder.jp/contests/abc094/tasks/abc094_b

n, m, x = map(int, input().split())
a = list(map(int, input().split()))
to_n = 0
to_0 = 0

for i in a:
    if i < x:
        to_0 += 1
    else:
        to_n += 1

ans = min(to_0, to_n)
print(ans)

# 15:00 - 15:29


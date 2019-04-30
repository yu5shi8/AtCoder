# -*- coding: utf-8 -*-
# B - ISU
# https://atcoder.jp/contests/abc078/tasks/abc078_b

x, y, z = map(int, input().split())
count = x//(y+z)

if count*(y+z) + z <= x:
    print(count)
else:
    print(count-1)

# 10:05 - 10:33

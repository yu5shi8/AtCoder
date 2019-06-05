# -*- coding: utf-8 -*-
# A - 長方形
# https://atcoder.jp/contests/abc027/tasks/abc027_a

l1, l2, l3 = map(int, input().split())
l = [l1, l2, l3]
l.sort()

if l[0] == l[1]:
    print(l[2])
else:
    print(l[0])

# 16:33 - 16:37

# -*- coding: utf-8 -*-
# B - Polygon
# https://atcoder.jp/contests/abc117/tasks/abc117_b

n = int(input())
l = list(map(int, input().split()))
long = max(l)
if sum(l) - long > long:
    print('Yes')
else:
    print('No')

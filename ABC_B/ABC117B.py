# -*- coding: utf-8 -*-
# B - Polygon
# https://atcoder.jp/contests/abc117/tasks/abc117_b

n = int(input())
l = list(map(int, input().split()))

longest = max(l)
calc = sum(l) - longest

if calc > longest:
    print('Yes')
else:
    print('No')

# 15:36 - 15:41

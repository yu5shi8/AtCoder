# -*- coding: utf-8 -*-
# B - たてなが / Thin
# https://atcoder.jp/contests/abc049/tasks/abc049_b

h, w = map(int, input().split())
a = [input()*2 for _ in range(h)]

for i in range (h):
    print(a[i][:w])
    print(a[i][w:])

# 10:35 - 10:54

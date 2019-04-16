# -*- coding: utf-8 -*-
# ABC085B - Kagami Mochi
# https://atcoder.jp/contests/abs/tasks/abc085_b

n = int(input())
l = []

for i in range(n):
    d = int(input())
    l.append(d)

ans = len(list(set(l)))
print(ans)
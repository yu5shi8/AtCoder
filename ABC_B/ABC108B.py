# -*- coding: utf-8 -*-
# B - Ruined Square
# https://atcoder.jp/contests/abc108/tasks/abc108_b

x1, y1, x2, y2 = map(int, input().split())

x = x2 - x1
y = y2 - y1

print(x2-y, x+y2, x1-y, x+y1)

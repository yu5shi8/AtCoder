# -*- coding: utf-8 -*-
# B - 錠
# https://atcoder.jp/contests/abc013/tasks/abc013_2

a = int(input())
b = int(input())

x = abs(a - b)
y = min(a, b) + 10 - max(a, b)

print(min(x, y))

# 22:32 - 22:40（AC）

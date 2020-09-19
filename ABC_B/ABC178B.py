# -*- coding: utf-8 -*-
# B - Product Max
# https://atcoder.jp/contests/abc178/tasks/abc178_b

a, b, c, d = map(int, input().split())

check = [a * c, a * d, b * c, b * d]

print(max(check))

# 21:01 - 21:05（AC）

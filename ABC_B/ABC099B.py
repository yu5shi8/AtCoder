# -*- coding: utf-8 -*-
# B - Stone Monument
# https://atcoder.jp/contests/abc099/tasks/abc099_b

a, b = map(int, input().split())
a_hight = 0
calc = b - a

for i in range(1, calc):
    a_hight += i

print(a_hight - a)

# 11:36 - 13:15

# -*- coding: utf-8 -*-
# B - Multiple of 9
# https://atcoder.jp/contests/abc176/tasks/abc176_b

N = input()
check = 0

for n in N:
    check += int(n)

if check % 9 == 0:
    print('Yes')
else:
    print('No')

# 18:08 - 18:13（AC）

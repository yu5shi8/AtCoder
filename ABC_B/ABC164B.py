# -*- coding: utf-8 -*-
# B - Battle
# https://atcoder.jp/contests/abc164/tasks/abc164_b

A, B, C, D = map(int, input().split())
Flag = 1

while A > 0 and C > 0:
    if Flag == 1:
        C -= B
        Flag = 2
    else:
        A -= D
        Flag = 1

if Flag == 2:
    print('Yes')
else:
    print('No')

# 16:36 - 16:46（WA）- 16:57（AC）

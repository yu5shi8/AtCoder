# -*- coding: utf-8 -*-
# A - Rainy Season
# https://atcoder.jp/contests/abc175/tasks/abc175_a

S = input()

if S == 'RRR':
    print(3)
elif S[:2] == 'RR' or S[1:] == 'RR':
    print(2)
elif S[0] == 'R' or S[1] == 'R' or S[2] == 'R':
    print(1)
else:
    print(0)

# 15:14 - 15:18（AC）

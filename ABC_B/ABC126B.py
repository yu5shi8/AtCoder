# -*- coding: utf-8 -*-
# B - YYMM or MMYY
# https://atcoder.jp/contests/abc126/tasks/abc126_b

s = input()
left = int(s[:2])
right = int(s[2:])

if 1 <= left <= 12 and 1 <= right <= 12:
    print('AMBIGUOUS')
elif 1 <= right <= 12:
    print('YYMM')
elif 1 <= left <= 12:
    print('MMYY')
else:
    print('NA')

# 21:08 - 21:19

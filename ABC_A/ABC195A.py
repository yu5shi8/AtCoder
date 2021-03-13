# -*- coding: utf-8 -*-
# A - Health M Death
# https://atcoder.jp/contests/abc195/tasks/abc195_a

M, H = map(int, input().split())
check = H / M

if check.is_integer():
    print('Yes')
else:
    print('No')

# 21:00 - 21:03（AC）

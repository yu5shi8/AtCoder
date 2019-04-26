# -*- coding: utf-8 -*-
# B - Postal Code
# https://atcoder.jp/contests/abc084/tasks/abc084_b

a, b = map(int, input().split())
s = input()

if s[a] == '-' and s[:a].isdigit() and s[a+1:].isdigit():
    print('Yes')
else:
    print('No')


# 18:15 - 18:35

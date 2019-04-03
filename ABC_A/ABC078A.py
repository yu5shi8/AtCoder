# -*- coding: utf-8 -*-
# A - HEX
# https://atcoder.jp/contests/abc078/tasks/abc078_a

x, y = input().split()
l = {'A':10, 'B':11, 'C':12, 'D':13, 'E':14, 'F':15}

if l[x] < l[y]:
    print('<')
elif l[x] > l[y]:
    print('>')
else:
    print('=')

# -*- coding: utf-8 -*-
# A - Wanna go back home
# https://atcoder.jp/contests/agc003/tasks/agc003_a

S = input()

if 'N' in S:
    if 'S' not in S:
        print('No')
        exit()
if 'S' in S:
    if 'N' not in S:
        print('No')
        exit()
if 'E' in S:
    if 'W' not in S:
        print('No')
        exit()
if 'W' in S:
    if 'E' not in S:
        print('No')
        exit()

print('Yes')

# 17:26 - 17:38（AC）

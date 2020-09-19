# -*- coding: utf-8 -*-
# A - Plural Form
# https://atcoder.jp/contests/abc179/tasks/abc179_a

S = input()

if S[-1] == 's':
    S += 'es'
else:
    S += 's'

print(S)

# 21:00 - 21:01（AC）

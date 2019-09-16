# -*- coding: utf-8 -*-
# B - Tap Dance
# https://atcoder.jp/contests/abc141/tasks/abc141_b

S = input()

for i in range(len(S)):
    if i % 2 != 0:
        if S[i] == 'R':
            print('No')
            exit()
    else:
        if S[i] == 'L':
            print('No')
            exit()

print('Yes')

# 16:09 - 16:14（AC）

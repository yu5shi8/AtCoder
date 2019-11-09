# -*- coding: utf-8 -*-
# A - DEAD END
# https://atcoder.jp/contests/arc021/tasks/arc021_1

A1 = list(map(int, input().split()))
A2 = list(map(int, input().split()))
A3 = list(map(int, input().split()))
A4 = list(map(int, input().split()))

for i in range(1, 4):
    if A1[i-1] == A1[i] or A2[i-1] == A2[i] or A3[i-1] == A3[i] or A4[i-1] == A4[i]:
        print('CONTINUE')
        exit()

for i in range(4):
    if A1[i] == A2[i] or A2[i] == A3[i] or A3[i] == A4[i]:
        print('CONTINUE')
        exit()

print('GAMEOVER')

# 13:57 - 14:27（AC）

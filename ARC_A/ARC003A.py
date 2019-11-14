# -*- coding: utf-8 -*-
# A - GPA計算
# https://atcoder.jp/contests/arc003/tasks/arc003_1

N = int(input())
r = input()
cnt = 0

for i in range(N):
    if r[i] == 'A':
        cnt += 4
    elif r[i] == 'B':
        cnt += 3
    elif r[i] == 'C':
        cnt += 2
    elif r[i] == 'D':
        cnt += 1
    else:
        cnt += 0

gpa = cnt / N

print('{:.12f}'.format(gpa))

# 15:10 - 15:14（AC）

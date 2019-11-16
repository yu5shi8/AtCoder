# -*- coding: utf-8 -*-
# B - 音楽ゲーム
# https://atcoder.jp/contests/arc016/tasks/arc016_2

N = int(input())
x = [input() for _ in range(N)]
y = [''] * 9
cnt = 0

for i in range(N):
    for j in range(9):
        y[j] += x[i][j]

for i in range(9):
    for j in range(N):
        if y[i][j] == 'x':
            cnt += 1
        if y[i][j] == 'o':
            cnt += 1
            if 0 < j and y[i][j-1] == y[i][j]:
                cnt -= 1

print(cnt)

# 17:56 - 18:45（AC）

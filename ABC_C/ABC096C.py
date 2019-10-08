# -*- coding: utf-8 -*-
# C - Grid Repainting 2
# https://atcoder.jp/contests/abc096/tasks/abc096_c

H, W = map(int, input().split())
s = [list(input()) for _ in range(H)]
ng = 0

for i in range(1, H):
    for j in range(1, W):
        if s[i][j] == '#':
            if i < H - 1 and j < W - 1:
                if '#' not in [s[i-1][j], s[i+1][j], s[i][j-1], s[i][j+1]]:
                    ng += 1
            elif i == H - 1 and j == W - 1:
                if '#' not in [s[i-1][j], s[i][j-1]]:
                    ng += 1
            elif j == W - 1:
                if '#' not in [s[i-1][j], s[i+1][j], s[i][j-1]]:
                    ng += 1
            elif i == H - 1:
                if '#' not in [s[i-1][j], s[i][j-1], s[i][j+1]]:
                    ng += 1
    if ng > 0:
        print('No')
        exit()

print('Yes')

# 10:51 - 11:28（AC）

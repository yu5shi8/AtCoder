# -*- coding: utf-8 -*-
# B - Minesweeper
# https://atcoder.jp/contests/abc075/tasks/abc075_b

h, w = map(int, input().split())
s = [list(input()) for i in range(h)]
ans = [list('0')*w for i in range(h)]
temp = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1),
        (1, -1), (1, 0), (1, 1)]

for i in range(h):
    for j in range(w):
        if s[i][j] == '#':
            ans[i][j] = '#'
        else:
            count = 0
            for k in temp:
                i_temp, j_temp = i+k[0], j+k[1]
                if 0 <= i_temp < h and 0 <= j_temp < w:
                    if s[i_temp][j_temp] == '#':
                        count += 1
            ans[i][j] = count
    print(*ans[i], sep='')

# 0:39 - 3:36

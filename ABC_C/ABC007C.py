# -*- coding: utf-8 -*-
# C - 幅優先探索
# https://atcoder.jp/contests/abc007/tasks/abc007_3

from collections import deque

R, C = map(int, input().split())
sy, sx = map(int, input().split())
gy, gx = map(int, input().split())
c = [input() for _ in range(R)]

sy, sx, gy, gx = sy-1, sx-1, gy-1, gx-1
dist = [[-1]*C for _ in range(R)]
dist[sy][sx] = 0

que = deque()
que.append((sy, sx))

while que:
    y, x = que.popleft()

    if y == gy and x == gx:
        print(dist[y][x])
        exit()
    
    for dy, dx in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
        ny = y + dy
        nx = x + dx
        if c[ny][nx] == '.' and dist[ny][nx] == -1:
            que.append((ny, nx))
            dist[ny][nx] = dist[y][x] + 1

# [1] 19:07 - 19:59（写経）
# [2] 21:17 - 22:00（写経2）
# [3] 22:04 - 22:25（AC）

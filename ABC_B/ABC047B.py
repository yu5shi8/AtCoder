# -*- coding: utf-8 -*-
# B - すぬけ君の塗り絵 2 イージー / Snuke's Coloring 2 (ABC Edit)
# https://atcoder.jp/contests/abc047/tasks/abc047_b

w, h, n = map(int, input().split())
xya = [list(map(int, input().split())) for _ in range(n)]
xwyh = [0, w, 0, h]

for i in range(n):
    x = xya[i][0]
    y = xya[i][1]
    a = xya[i][2]
    if a == 1:
        xwyh[0] = max(x, xwyh[0])
    if a == 2:
        xwyh[1] = min(x, xwyh[1])
    if a == 3:
        xwyh[2] = max(y, xwyh[2])
    if a == 4:
        xwyh[3] = min(y, xwyh[3])

dw = max(xwyh[1] - xwyh[0], 0)
dh = max(xwyh[3] - xwyh[2], 0)

print(dw * dh)

# 15:37 - 16:01（WJ... -> WA）-（解説・解答を閲覧）17:50（AC）

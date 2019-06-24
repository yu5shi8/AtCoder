# -*- coding: utf-8 -*-
# B - Grid Compression
# https://atcoder.jp/contests/abc107/tasks/abc107_b

h, w = map(int, input().split())
a = [list(input()) for _ in range(h)]

tate = [False] * h
yoko = [False] * w

for i in range(h):
    for j in range(w):
        if a[i][j] == '#':
            tate[i] = True
            yoko[j] = True

for i in range(h):
    if tate[i]:
        for j in range(w):
            if yoko[j]:
                print(a[i][j], end='')
        print()

# 16:52 - 18:55（わかりませんでした）
# 19:50 - 19:59、21:53 - 22:44（わかりませんでした）
#（解説・解答を閲覧）- 23:34 - （再挑戦）23:39（AC）

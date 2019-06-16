# -*- coding: utf-8 -*-
# C - Rectangle Cutting
# https://atcoder.jp/contests/abc130/tasks/abc130_c

w, h, x, y = map(int, input().split())
ans = []

if w == x*2 and h == y*2:
    ans.append('{:.7f}'.format(w*h/2))
    ans.append(1)
else:
    ans.append('{:.7f}'.format(w*h/2))
    ans.append(0)

print(*ans, sep=' ')

# 21:13 - 22:01（WA）（わかりませんでした）
#（解説・解答を閲覧してAC）

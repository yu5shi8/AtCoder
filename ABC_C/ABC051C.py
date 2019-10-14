# -*- coding: utf-8 -*-
# C - Back and Forth
# https://atcoder.jp/contests/abc051/tasks/abc051_c

sx, sy, tx, ty = map(int, input().split())

x = tx - sx
y = ty - sy

ans = 'U'*y + 'R'*x + 'D'*y + 'L'*x
ans += 'L' + 'U'*(y+1) + 'R'*(x+1) + 'D'
ans += 'R' + 'D'*(y+1) + 'L'*(x+1) + 'U'

print(ans)

# [1] 15:56 -（さっぱり分かりません / 解説・解答を閲覧）17:12（AC）
# [2] 17:39 - 17:47（AC）

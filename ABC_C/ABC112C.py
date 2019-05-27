# -*- coding: utf-8 -*-
# C - Pyramid
# https://atcoder.jp/contests/abc112/tasks/abc112_c

n = int(input())
xyh = [list(map(int, input().split())) for _ in range(n)]
xyh.sort(key=lambda x: -x[2])

for cx in range(101):
    for cy in range(101):
        ch = None
        for x, y, h in xyh:
            t = h + abs(cx - x) + abs(cy - y)
            if h > 0:
                if ch is not None and t != ch:
                    break
                ch = t
            else:
                if t < ch:
                    break
        else:
            print(cx, cy, ch)
            exit()

# 16:11 - 17:02
#（解説・解答を閲覧）- 17:46
#（穴埋め解答）- 17:55
#（再挑戦）18:21 - 18:39
#（再々挑戦）18:39 - 18:45（WA）- 18:47（AC）

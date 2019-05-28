# -*- coding: utf-8 -*-
# C - Pyramid
# https://atcoder.jp/contests/abc112/tasks/abc112_c

n = int(input())
xyh = [list(map(int, input().split())) for i in range(n)]
xyh.sort(key=lambda x:-x[2])

for cx in range(101):
    for cy in range(101):
        ch = None
        for x, y, h in xyh:
            t = h + abs(x-cx) + abs(y-cy)
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

# 22:28 - 22:41

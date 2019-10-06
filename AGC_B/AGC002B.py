# -*- coding: utf-8 -*-
# B - Box and Ball
# https://atcoder.jp/contests/agc002/tasks/agc002_b

N, M = map(int, input().split())
box = [1] * N
red = [False] * N
red[0] = True

for i in range(M):
    x, y = map(int, input().split())
    if red[x-1] == True:
        red[y-1] = True
        box[x-1] -= 1
        box[y-1] += 1
    else:
        box[x-1] -= 1
        box[y-1] += 1
    if box[x-1] == 0:
        red[x-1] = False

ans = red.count(True)
print(ans)

# 14:03 - 14:10（WA）/ 14:47 - 14:56（WA）- 15:06（WA / 解説を閲覧）- 15:17（AC）

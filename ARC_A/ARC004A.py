# -*- coding: utf-8 -*-
# A - 2点間距離の最大値 ( The longest distance )
# https://atcoder.jp/contests/arc004/tasks/arc004_1

N = int(input())
xy = [list(map(int, input().split())) for _ in range(N)]
ans = 0

for i in range(N):
    for j in range(i, N):
        if i != j:
            num = pow((xy[j][0] - xy[i][0])**2 + (xy[j][1] - xy[i][1])**2, 0.5)
            if ans < num:
                ans = num

print('{:.6f}'.format(ans))

# 14:02 - 14:12（AC）

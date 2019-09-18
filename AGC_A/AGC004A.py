# -*- coding: utf-8 -*-
# A - Divide a Cuboid
# https://atcoder.jp/contests/agc004/tasks/agc004_a

ABC = list(map(int, input().split()))
ABC.sort()
num = ABC[-1] // 2

red = ABC[0] * ABC[1] * num
blue = ABC[0] * ABC[1] * (ABC[-1] - num)

ans = abs(red - blue)
print(ans)

# 20:32 - 20:36 / 20:50 - 20:53（AC）

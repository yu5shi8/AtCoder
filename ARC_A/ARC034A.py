# -*- coding: utf-8 -*-
# A - 首席
# https://atcoder.jp/contests/arc034/tasks/arc034_1

N = int(input())
member = [0] * N

for i in range(N):
    a, b, c, d, e = map(int, input().split())
    e *= 110 / 900
    score = a + b + c + d + e
    member[i] = score

print(max(member))

# 14:44 - 14:46（AC）

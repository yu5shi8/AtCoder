# -*- coding: utf-8 -*-
# B - 真冬日？真夏日？
# https://atcoder.jp/contests/arc015/tasks/arc015_2

N = int(input())
ans = [0] * 6

for i in range(N):
    a, b = map(float, input().split())
    if a >= 35:
        ans[0] += 1
    elif 30 <= a < 35:
        ans[1] += 1
    elif 25 <= a < 30:
        ans[2] += 1
    if 25 <= b:
        ans[3] += 1
    elif b < 0 and 0 <= a:
        ans[4] += 1
    elif a < 0:
        ans[5] += 1

print(*ans, sep=' ')

# 16:43 - 16:50（AC）

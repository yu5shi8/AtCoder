# -*- coding: utf-8 -*-
# C - Colorful Leaderboard
# https://atcoder.jp/contests/abc064/tasks/abc064_c

n = int(input())
a = list(map(int, input().split()))

ans = [0] * 8
free = 0

for i in range(n):
    if 1 <= a[i] <= 399:
        ans[0] += 1
    elif 400 <= a[i] <= 799:
        ans[1] += 1
    elif 800 <= a[i] <= 1199:
        ans[2] += 1
    elif 1200 <= a[i] <= 1599:
        ans[3] += 1
    elif 1600 <= a[i] <= 1999:
        ans[4] += 1
    elif 2000 <= a[i] <= 2399:
        ans[5] += 1
    elif 2400 <= a[i] <= 2799:
        ans[6] += 1
    elif 2800 <= a[i] <= 3199:
        ans[7] += 1
    elif 3200 <= a[i]:
        free += 1

num = len(ans) - ans.count(0)
print(str(max(num, 1)) + ' ' + str(num + free))

# 15:31 - 15:50（AC）

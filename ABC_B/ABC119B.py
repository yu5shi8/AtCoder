# -*- coding: utf-8 -*-
# B - Digital Gifts
# https://atcoder.jp/contests/abc119/tasks/abc119_b

n = int(input())
xu = [list(input().split()) for _ in range(n)]
btc = 380000.0
ans = float(0)

for i in range(n):
    count = 0
    if xu[i][1] == 'JPY':
        ans += int(xu[i][0])
    else:
        ans += btc * float(xu[i][0])

print('{:.7f}'.format(ans))

# 20:52 - 21:19

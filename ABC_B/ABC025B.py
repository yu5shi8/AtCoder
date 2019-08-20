# -*- coding: utf-8 -*-
# B - 双子とスイカ割り
# https://atcoder.jp/contests/abc025/tasks/abc025_b

n, a, b = map(int, input().split())
east = []
west = []

for i in range(n):
    sd = list(input().split())
    if int(sd[1]) < a:
        sd[1] = a
    elif int(sd[1]) > b:
        sd[1] = b
    else:
        sd[1] = int(sd[1])
    if sd[0] == 'East':
        east.append(sd[1])
    else:
        west.append(sd[1])

if sum(east) > sum(west):
    ew = 'East'
else:
    ew = 'West'

num = abs(sum(east) - sum(west))

if num != 0:
    print(ew + ' ' +str(num))
else:
    print(num)

# 16:14 - 16:31（AC）

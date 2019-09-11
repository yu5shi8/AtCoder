# -*- coding: utf-8 -*-
# B - Evilator
# https://atcoder.jp/contests/agc015/tasks/agc015_b

S = input()
N = len(S)
count = 0

for i in range(N):
    top = ((N-1) - i)
    btm = i
    if S[i] == 'U':
        count += (btm*2 + top)
    else:
        count += (btm + top*2)

print(count)

# 11:25 - 12:11（論理立て）- 12:21（TLE）- 12:24（TLE）- 12:44（AC）

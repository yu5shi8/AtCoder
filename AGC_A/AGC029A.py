# -*- coding: utf-8 -*-
# A - Irreversible operation
# https://atcoder.jp/contests/agc029/tasks/agc029_a

S = input()
N = len(S)
ans = 0

cnt_B = S.count('B')
idx_B = N - cnt_B

for i in range(N):
    if S[i] == 'B':
        ans += idx_B - i
        idx_B += 1

print(ans)

# 15:37 - 16:10（TLE）- 17:58（AC）

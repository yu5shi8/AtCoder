# -*- coding: utf-8 -*-
# B - Go to Jail
# https://atcoder.jp/contests/abc179/tasks/abc179_b

N = int(input())
cnt = 0

for i in range(N):
    D1, D2 = map(int, input().split())
    if D1 == D2:
        cnt += 1
    else:
        cnt = 0
    if cnt >= 3:
        print('Yes')
        exit()

print('No')

# 21:01 - 21:08（AC）

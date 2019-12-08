# -*- coding: utf-8 -*-
# B - 割り切れる日付
# https://atcoder.jp/contests/arc002/tasks/arc002_2

Y, M, D = map(int, input().split('/'))

def is_leap(y):
    if y % 4 == 0:
        if y % 100 != 0 or y % 400 == 0:
            return 1
    return 0

days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

while (1):
    if is_leap(Y) == 1:
        days[1] = 29
    else:
        days[1] = 28
    if Y % M == 0 and Y / M % D == 0:
        print(str(Y).zfill(4) + '/' + str(M).zfill(2) + '/' + str(D).zfill(2))
        exit()
    D += 1
    if D > days[M-1]:
        D = 1
        M += 1
    if M > 12:
        M = 1
        Y += 1

# [1] 21:46 - 22:35（TLE）- 22:49 / 14:13 - 14:35（WA）- 14:48（WA）- 14:52（WA）- 15:01（WA）- 15:08（AC）
# [2] 15:16 - 15:26（AC）

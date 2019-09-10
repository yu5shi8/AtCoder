# -*- coding: utf-8 -*-
# C - Bugged
# https://atcoder.jp/contests/abc063/tasks/arc075_a

N = int(input())
S = [int(input()) for _ in range(N)]
S.sort()
sum_s = sum(S)

if sum_s % 10 != 0:
    print(sum_s)
    exit()

for s in S:
    if (sum_s - s) % 10 != 0:
        print(sum_s - s)
        exit()

print(0)

# [1] 11:20 - 11:23（WA）- 11:23（WA）（解説を閲覧）11:34（WA）-（解答を閲覧）11:43
# [2] 13:49 - 13:53（AC）

# -*- coding: utf-8 -*-
# C - 4-adjacent
# https://atcoder.jp/contests/abc069/tasks/arc080_a

N = int(input())
A = list(map(int, input().split()))
num_2 = 0
num_4 = 0
odd = 0

for i in range(N):
    if A[i] % 2 != 0:
        odd += 1
    elif A[i] % 4 == 0:
        num_4 += 1
    else:
        num_2 += 1

if num_2 == 0:
    if odd - 1 <= num_4:
        print('Yes')
    else:
        print('No')
else:
    if odd <= num_4:
        print('Yes')
    else:
        print('No')

# 20:36 - 22:53（WA）- 22:58（解説を閲覧）- 23:05（WA）-（解答を閲覧）23:11（WA）- 23:24（AC）

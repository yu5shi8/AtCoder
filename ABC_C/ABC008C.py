# -*- coding: utf-8 -*-
# C - コイン
# https://atcoder.jp/contests/abc008/tasks/abc008_3

N = int(input())
C = [int(input()) for _ in range(N)]
ans = 0

for i in range(N):
    S = 0
    for j in range(N):
        if i != j and C[i] % C[j] == 0:
            S += 1
    if S % 2 == 0:
        ans += (S+2)/(2*S+2)
    else:
        ans += 1/2

print('{:.12f}'.format(ans))

# [1] 15:07 - 16:54（解説・解答を閲覧）
# [2] 17:11 - 17:17（AC）

# -*- coding: utf-8 -*-
# A - AtCoder Group Contest
# https://atcoder.jp/contests/agc012/tasks/agc012_a

N = int(input())
a = list(map(int, input().split()))
a.sort()
score = 0

for i in range(N, N*3, 2):
    score += a[i]

print(score)

# [1] 9:00 - 9:24（WA）- 9:52（WA）（もう分からない / 解説を閲覧）- 10:27（WA）-（解答を閲覧）10:30（AC）
# [2] 13:31 - 13:35（AC）

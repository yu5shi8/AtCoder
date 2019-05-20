# -*- coding: utf-8 -*-
# C - Dice and Coin
# https://atcoder.jp/contests/abc126/tasks/abc126_c

n, k = map(int, input().split())
ans = 0

for i in range(1, n+1):
    count = 0
    if i >= k:
        ans += 1 / n
    else:
        count = 1
        while i * 2**count < k:
            count += 1
        num = (1/n) * (0.5**count)
        ans += num

print('{:.12f}'.format(ans))

# 20:32 - 20:48（WA）
# （解答を閲覧）- 21:06

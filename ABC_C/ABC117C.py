# -*- coding: utf-8 -*-
# C - Streamline
# https://atcoder.jp/contests/abc117/tasks/abc117_c

n, m = map(int, input().split())
x = sorted(list(map(int, input().split())))
count = [0] * (m-1)
ans = 0

if n > m:
    ans += 0
else:
    for i in range(1, m):
        count[i-1] = x[i] - x[i-1]
    count = sorted(count, reverse=True)
    ans = sum(count[n-1:])

print(ans)


# 15:44 - 16:19（WA）
# （解説・解答を閲覧）- 16:27

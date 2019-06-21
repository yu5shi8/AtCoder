# -*- coding: utf-8 -*-
# C - Triangular Relationship
# https://atcoder.jp/contests/abc108/tasks/arc102_a

n, k = map(int, input().split())
ans = 0

if k % 2 != 0:
    ans += (n // k) ** 3
else:
    ans += (n // k) ** 3
    ans += ((n + k // 2) // k) ** 3

print(ans)

# 21:27 - 21:53
#（解説・解答を閲覧）- 24:17（AC）

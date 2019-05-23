# -*- coding: utf-8 -*-
# C - Christmas Eve
# https://atcoder.jp/contests/abc115/tasks/abc115_c

n, k = map(int, input().split())
h = sorted(list(int(input()) for _ in range(n)))
ans = []

for i in range(n-k+1):
    ans.append(h[i+k-1] - h[i])

print(min(ans))

# 10:24 - 11:35（WA）
#（解説・解答を閲覧）- 11:48
#（穴埋め）16:33 - 16:42

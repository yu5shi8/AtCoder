# -*- coding: utf-8 -*-
# C - Grand Garden
# https://atcoder.jp/contests/abc116/tasks/abc116_c

n = int(input())
h = list(map(int, input().split()))
ans = h[0]

for i in range(1, n):
    if h[i] > h[i-1]:
        ans += h[i] - h[i-1]

print(ans)

# 9:07 - 10:55
# 16:47 - 17:41
#（解説・解答を参照）- 17:55
#（穴埋め）- 17:58
#（復習）- 18:01

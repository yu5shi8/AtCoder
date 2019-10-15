# -*- coding: utf-8 -*-
# C - 単調増加
# https://atcoder.jp/contests/abc038/tasks/abc038_c

N = int(input())
a = list(map(int, input().split()))
l, r, ans = 0, 0, 0

for i in a:
    if r < i:
        l += 1
    else:
        l = 1
    ans += l
    r = i

print(ans)

# [1] 17:30 - 18:03（WA）- 19:01（WA / 解説・解答を閲覧）19:19
# [2] 19:23 - 19:35（AC）
